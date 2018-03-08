import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                    'computing_comms_project.settings')

import django
django.setup()
from computingcomms.models import Quiz, Question, Answer


def populate():
    OOSEQ1ANS = {"0000":{ "correct":False, "content":"A type of coffee"},
                 "0001": {"correct":True, "content":"A programming Language"}
                 }

    WAD2Q1ANS = {"0000":{"correct":True, "content":"A programme used to browse the internet"},
                 "0001":{"correct":False, "content":"An enemy in Mario"}}
    
    OOSEQuestions = {"Question 1":{"answers":OOSEQ1ANS,"content":"What is java in the context of CS?"}}
    
    WAD2Questions = {"Question 1":{"answers":WAD2Q1ANS,"content":"What is a browser?"}}

    quizzes = {"OOSE Quiz 1": {"questions":OOSEQuestions,"ID":"0000","subject":"OOSE"},
               "WAD2 Quiz 1": {"questions":WAD2Questions, "ID":"0001", "subject":"WAD2"}
               }
    
    for quiz, quiz_content in quizzes.items():
        qz = add_quiz(quiz,quiz_content["subject"],quiz_content["ID"])
        for question, question_data in quiz_content["questions"].items():
            qu = add_question(question, qz, question_data["content"])
            for answer, answer_details in question_data["answers"].items():
                an = add_answer(answer,qu,answer_details["correct"],answer_details["content"])
                

def add_answer(ID, question, correct, content):
    an = Answer.objects.get_or_create(answerID = ID, question = question)[0]
    an.correct = correct
    an.content = content
    an.save()
    return an
        
def add_question(name, quiz, content):
    qu = Question.objects.get_or_create(name=name, quiz=quiz)[0]
    qu.content = content
    qu.save()
    return qu

def add_quiz(name, subject, ID):
    qz = Quiz.objects.get_or_create(name=name)[0]
    qz.quizID = ID
    qz.subject=subject
    qz.save()
    return qz

# Start execution here!
if __name__ == '__main__':
    print("Make some quizzes!")
    populate()
    print("Done!")
