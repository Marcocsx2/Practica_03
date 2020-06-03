from django.db import models
import json


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    nationality = models.CharField(max_length=50)

    # def __str__(self):
    #     return self.name


class Book(models.Model):

    id = models.IntegerField(primary_key=True)
    code = models.IntegerField(null=True)
    tittle = models.CharField(max_length=100)
    isbn = models.CharField(max_length=30)
    editorial = models.CharField(max_length=60)
    pageNumber = models.IntegerField(null=True, db_column='page_number')
    author = models.ForeignKey(
        Author, null=True, related_name='books', on_delete=models.CASCADE)
    # idAuthor = models.ForeignKey(Author, on_delete=models.DO_NOTHING)

    # def __str__(self):
    #     return self.tittle


class User(models.Model):

    id = models.IntegerField(primary_key=True)
    numUser = models.IntegerField(db_column='num_user')
    dni = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    phoneNumber = models.CharField(db_column='phone_number', max_length=255)

    def __str__(self):
        return self.name


class Lend(models.Model):

    id = models.IntegerField(primary_key=True)
    book = models.ForeignKey(
        Book,
        db_column='book_id',
        null=True,
        # related_name='lends',
        on_delete=models.CASCADE)
    user = models.ForeignKey(
        User,
        db_column='user_id',
        null=True,
        # related_name='lends',
        on_delete=models.CASCADE)
    lendDate = models.DateTimeField(db_column='lend_date', auto_now=True)
    returnDate = models.DateTimeField(db_column='return_date', auto_now=True)
