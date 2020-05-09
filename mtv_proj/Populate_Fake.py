import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','mtv_proj.settings')
import django
django.setup()

from mtv_app.models import User
from faker import Faker

fakegen = Faker()

def add_fake_user(n=10):
    for entry in range(n):
        fake_firstname = fakegen.first_name()
        fake_lastname = fakegen.last_name()
        fake_email = fakegen.email()

        t = User.objects.get_or_create(first_name=fake_firstname,last_name=fake_lastname,email=fake_email)[0]
        t.save()
if __name__ == '__main__':
    print ("Populating Users..")

add_fake_user(20)
