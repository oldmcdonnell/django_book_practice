import os
import django
from django.conf import settings
# Use this by running:
# python standalone_script.py
os.environ["DJANGO_SETTINGS_MODULE"] = "django_project.settings"
django.setup()

from django_app.models import *

print('SCRIPT START *************************')
# Now you have django, so you can import models and do stuff as normal
### NOTE
# DO NOT CHANGE CODE ABOVE THIS LINE
# WORK BELO

# Author.objects.bulk_create(
#  [
#     Author(name='John'),
#     Author(name='Bob'),
#     Author(name='Lisa'),
#     Author(name='Frank'),
#     Author(name='Julia'),
#     Author(name='Simon'),
#     Author(name='Paul'),
#     Author(name='Satan')
#  ]
# )

# authors = Author.objects.all()
# print(authors)


# Book.objects.bulk_create(
#     [
#         Book(title='The Satan Bible'),
#         Book(title='Paul book'),
#         Book(title='Yellow Book'),
#         Book(title='The Express'),
#         Book(title='Skull and Bones'),
#         Book(title='Green Goo'),
#         Book(title='The other secret'),
#         Book(title='Julia finds a way'),
#         Book(title='The Van'),
#         Book(title='John little book'),
#         Book(title='The Glass Onion')

#     ]
# )

# books = Book.objects.all()
# print(books)


# book = Book.objects.get(title='Julia finds a way')
# book.author = Author.objects.get(name='Julia')
# book.save()


auth = Author.objects.get(name='John')
book1 = Book.objects.get(title='Green Goo')
book2 = Book.objects.get(title='The Van')
book3 = Book.objects.get(title='John little book')

auth.book_set.add(book1, book2, book3)

print(auth.name, auth.book_set.all())