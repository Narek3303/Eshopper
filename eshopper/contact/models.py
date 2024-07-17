from django.db import models

class ContactUs(models.Model):
    name = models.CharField('Name: ', max_length=50)
    subject = models.CharField('Subject: ', max_length=100)
    email = models.EmailField('Email: ')
    comment = models.TextField('Comment: ')


    def __str__(self):
        return self.name



class ContactInformation(models.Model):
    text = models.TextField('Text: ')
    title = models.CharField('Title: ', max_length=50)
    address = models.CharField('Adress: ', max_length=50)
    info = models.CharField('Info: ', max_length=50)
    number = models.CharField('Number: ', max_length=50)


    def __str__(self):
        return self.title




