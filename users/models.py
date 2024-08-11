import random
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core import validators
from django.utils import timezone
from django.contrib.auth.models import AbstractUser,PermissionsMixin,BaseUserManager,send_mail


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, phone_number, email, password,is_staff,is_superuser,**extra_fields):
        now = timezone.now()
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        user = self.model(phone_number=phone_number,
                          username=username,
                          email=email,
                          is_staff=is_staff,
                          is_superuser=is_superuser,
                          date_joined=now,
                          **extra_fields)
        
        if not extra_fields.get('no_password'):
            user.set_password(password)
        user.save()
        return user

    def create_user(self, username=None, phone_number=None, email=None, password=None,is_staff=None,is_superuser=None,**extra_fields):
        if username is None:
            if email:
                username = email.split('@', 1)[0]
            if phone_number:
                username = random.choice('abcdefghijklmnopqrstuvwxyz') +str(phone_number)[-7:]
            while User.objects.filter(username=username).exists():
                username += str(random.randint(10,99))
        
        return self._create_user(username, phone_number, email, password, False,False, **extra_fields)
    
    def creat_superuser(self, username, phone_number, email, password,**extra_fields):
        return self._create_user(username, phone_number, email, password,True,True,**extra_fields)
    
    def get_by_phone_number(self, phone_number):
        return self.get(**{'phone_number': phone_number})
class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=32, unique=True,
                                help_text='Required. 30 characters or fewer string whit a letter.',
                                validators=[
                                    validators.RegexValidator('r^[a-zA-Z][a-zA-Z0-9_\.]+$',
                                                              'Enter a valid username starting with a-z.',
                                                              'This value may contain only letters, numbers',
                                                              'and underscores characters.', 'invalid',
                                                            )
                                ])
                            

    
    