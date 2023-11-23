import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'project2.settings')

import django
django.setup()


from faker import Faker
from app2.models import Student

fake = Faker()

def populate(n=20):
    for i in range(20):
        fakename = fake.name()
        fakelname = fake.name()
        fakeemail = fake.email()
        student = Student.objects.get_or_create(fname= fakename, lname= fakelname, email=fakeemail)[0]

print('populating')
populate()
print('populated')