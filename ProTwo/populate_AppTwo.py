import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

##FAKE POP SCRIPT

import random
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for entry in range(N):
        fake_name = fakegen.name().split()
        print(fake_name)
        fake_first_name = fake_name[0]
        print(fake_first_name)
        fake_last_name = fake_name[1]
        print(fake_last_name)
        fake_email = fakegen.email()

        user = User.objects.get_or_create(firstname=fake_first_name,lastname=fake_last_name,email=fake_email)[0]


if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("Populating complete")
