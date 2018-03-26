import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'computing_comms_project.settings')

import django
django.setup()
from computingcomms.models import ForumPost, Comment

def populate():

    WADComments = [{"comment": "You have to import django first.", "user": "Joe Bloggs", "date": "10/02/2018"}, {"comment": "What is your error message?", "user": "Anna Brown", "date": "14/01/2018"}]

    OOSEComments = [{"comment": "Did you count the else statement?", "user": "Mark Smith", "date": "01/02/2018"}, {"comment": "Did you count the blocks of code or the lines?", "user": "Harry Sharpe", "date": "19/02/2018"}, {"comment": "Did you use the equation V(G)=E-N+2?", "user": "Holly Byrne", "date": "21/02/2018"}]

    CFComments = [{"comment": "Did you use the commands SELECT, FROM and WHERE?", "user": "Russel Gordon", "date": "01/03/2018"}, {"comment": "Where you using more than one condition?", "user": "Martin Lyons", "date": "12/03/2018"}, {"comment": "What were you trying to display?", "user": "Laura Hill", "date": "22/03/2018"}]
