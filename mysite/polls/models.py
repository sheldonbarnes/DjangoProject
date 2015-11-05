# Create your models here.
import datetime
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from django.contrib.auth.models import User
from django import forms



class UserProfile(models.Model):

    user = models.OneToOneField(User)

    # The additional attributes we wish to include.
    website = models.URLField(blank=True)

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.user.username

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('user', 'website')

class Contact (models.Model):
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    PhoneNumber = models.CharField(max_length=20)
    EmailAddress = models.EmailField(max_length=254)
    Address = models.CharField(max_length=100)
    User = models.OneToOneField(User, default=2)
    #team_name = models.ForeignKey(UserProfile, default=0)
    #User_id = models.OneToOneField(User)
    def __str__(self):              # __unicode__ on Python 2
        return self.FirstName + " " + self.LastName

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):              # __unicode__ on Python 2
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

class Choice(models.Model):
    question = models.ForeignKey(Question)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.choice_text
