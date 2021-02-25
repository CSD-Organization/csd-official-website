from django.db import models

# Create your models here.
class ContactModel(models.Model):
    fname = models.TextField()
    lname = models.TextField()
    email = models.EmailField()
    phone_num = models.IntegerField()
    subject = models.TextField()
    message = models.TextField()
    send_on = models.DateTimeField()

    class Meta:
        verbose_name = 'User Contact'
        verbose_name_plural = 'User Contacts'

    def __str__(self) -> str:
        return f'{self.fname} {self.lname} says \'{self.subject}\'.'

class SubscribeModel(models.Model):
    email = models.EmailField()
    regdate = models.DateTimeField()

    class Meta:
        verbose_name = 'Subscribed User'
        verbose_name_plural = 'Subscribed Users'

    def __str__(self) -> str:
        return f'{self.email} registered on {self.regdate}'