from django.db import models

# Create your models here.
class Book:
    bookid:str
    name:str
    author:str
    publisher:str
    copies:int
    avl:int


