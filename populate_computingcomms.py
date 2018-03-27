import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'computing_comms_project.settings')

import django
django.setup()
from computingcomms.models import ForumPost, Comment, UserProfile
from django.contrib.auth.models import User

def populate():

    WADComments = [{"comment": "You have to import django first.", "user": "Joe Bloggs","pass":"kbhsda", "date": "10/02/2018"}, {"comment": "What is your error message?", "user": "Anna Brown","pass":"4kbvy32", "date": "14/01/2018"}]

    OOSEComments = [{"comment": "Did you count the else statement?", "user": "Mark Smith","pass":"fsDgfd", "date": "01/02/2018"}, {"comment": "Did you count the blocks of code or the lines?", "user": "Harry Sharpe", "pass":"easilyguessed", "date": "19/02/2018"}, {"comment": "Did you use the equation V(G)=E-N+2?", "user": "Holly Byrne","pass":"fs34432", "date": "21/02/2018"}]

    CFComments = [{"comment": "Did you use the commands SELECT, FROM and WHERE?", "user": "Russel Gordon", "pass":"bwejkser", "date": "01/03/2018"}, {"comment": "Were you using more than one condition?", "user": "Martin Lyons","pass":"nui432uib", "date": "12/03/2018"}, {"comment": "What were you trying to display?", "user": "Laura Hill", "pass":"dn93243242", "date": "22/03/2018"}]

    questions = {"Why am I getting a 'no module named Django' error message?": {"comments": WADComments,"user":["Keaton Greg","BadStorage"]}, "Why am I getting the wrong answer when working out the number of paths on my CFG diagram?": {"comments" : OOSEComments,"user":["Tracey Jones","ForReal"]}, "Why am I not getting any output when I am searching for a value I know exists in a database?": {"comments": CFComments,"user":["Nathan Fulton","Passwords"]}}

    for question, questions_data in questions.items():
        print("\n")
        q = add_q(question,questions_data["user"])
        for c in questions_data["comments"]:
            add_comment(q, c["comment"], c["user"], c["date"])

    for q in ForumPost.objects.all():
        for c in Comment.objects.filter(post=q):
            print("- {0} - {1}".format(str(q), str(c)))

def add_comment(question, comment, user, date):
    poster = User.objects.get_or_create(username=user,password="pass2")[0]
    c = Comment.objects.get_or_create(post=question, comment=comment, user=poster)[0]
    c.date = date
    c.save()
    return c

def add_q(question,data):
    print(data[0],type(data[0]))
    print(data[1],type(data[1]))
    here = User.objects.get_or_create(username=data[0],password=data[1])[0]
    q = ForumPost.objects.get_or_create(question=question,user=here)[0]
    q.save()
    return q

if __name__ == '__main__':
    print("Starting Computing Comms population script...")
    populate()
