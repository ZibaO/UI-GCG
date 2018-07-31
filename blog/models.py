from __future__ import unicode_literals

from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _
from .UserManager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('آدرس ایمیل'), unique=True)
    first_name = models.CharField(_('نام'), max_length=300, blank=True)
    last_name = models.CharField(_('نام خانوادگی'), max_length=300, blank=True)
    phone_number = models.CharField(_('شماره تلفن'), max_length=300, blank=True)
    national_number = models.CharField(_('شماره ملی'), max_length=300, blank=True)
    # location = models.CharField(_('شهر محل سکونت'), max_length=300, blank=True)
    username = models.CharField(_('نام کاربری'), max_length=300, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'site_informations'
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)

class Request(models.Model):

    text = models.TextField(_('درخواست'))
    writer = models.ForeignKey(User, on_delete=models.CASCADE)
    date_requested = models.DateTimeField(_('تاریخ ثبت درخواست'), auto_now_add=True)

    class Meta:
        db_table = 'Requests'
        verbose_name = _('request')
        verbose_name_plural = _('requests')






