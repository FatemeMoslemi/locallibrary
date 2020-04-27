from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a genre book (e.g. science fiction, french poetry , etc)')

    def __str__(self):
        return self.name

class book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL)
    summary = models.TextField(max_length=1000, help_text='Enter a description')
    isbn = models.CharField('isbn', max_length=200, help_text='')
