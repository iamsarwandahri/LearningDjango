import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'project1.settings')

import django
django.setup()


import random
from faker import Faker
from app1.models import Topic,Webpage,AccessRecords

fake = Faker()

topic = ['Social','Search','News','Sarwan','Sumair']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topic))[0]
    t.save()
    return t


def populate(n):
    
    for i in range(n):
        top = add_topic()
        fname = fake.company()
        furl = fake.url()
        fdate = fake.date()       
        
        wpage = Webpage.objects.get_or_create(topic=top,name=fname,url=furl)[0]
        
        acc = AccessRecords.objects.get_or_create(name=wpage,date=fdate)[0]
        

if __name__ == '__main__':
    print('Populating Script')
    populate(20)
    print('Populating Done')     
    