import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE",'modelforms.settings')

import django
django.setup()


from faker import Faker
from formsapp.models import Student

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