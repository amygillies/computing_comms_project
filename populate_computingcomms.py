import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'computing_comms_project.settings')

import django
django.setup()
from computingcomms.models import ForumPost, Comment

def populate():

    WADComments = [{"comment": "You have to import django first.", "user": "Joe Bloggs", "date": "10/02/2018"}, {"comment": "What is your error message?", "user": "Anna Brown", "date": "14/01/2018"}]

    OOSEComments = [{"comment": "Did you count the else statement?", "user": "Mark Smith", "date": "01/02/2018"}, {"comment": "Did you count the blocks of code or the lines?", "user": "Harry Sharpe", "date": "19/02/2018"}, {"comment": "Did you use the equation V(G)=E-N+2?", "user": "Holly Byrne", "date": "21/02/2018"}]

    CFComments = [{"comment": "Did you use the commands SELECT, FROM and WHERE?", "user": "Russel Gordon", "date": "01/03/2018"}, {"comment": "Were you using more than one condition?", "user": "Martin Lyons", "date": "12/03/2018"}, {"comment": "What were you trying to display?", "user": "Laura Hill", "date": "22/03/2018"}]

    questions = {"Why am I getting a 'no module named Django' error message?": {"comments": WADComments}, "Why am I getting the wrong answer when working out the number of paths on my CFG diagram?": {"comments" : OOSEComments}, "Why am I not getting any output when I am searching for a value I know exists in a database?" {"comments": CFComments}}

    for question, questions_data in questions.items():
        q = add_q(question)
        for c in questions_data["comments"]:
            add_comment(q, c["comment"], c["user"], c["date"])

    for q in ForumPost.objects.all():
        for c in Comments.objects.filter(question=q):
            print("- {0} - {1}".format(str(q), str(c)))

def add_comment(question, comment, user, date):
    c = Comment.objects.get_or_create(question=question, comment=comment)[0]
    c.user = user
    c.date = date
    c.save()
    return c

def add_q(question):
    q = ForumPost.objects.get_or_create(question=question)[0]
    q.save()
    return q

if __name__ == '__main__':
    print("Starting Computing Comms population script...")
    populate()
