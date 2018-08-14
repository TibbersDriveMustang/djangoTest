# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """
        Wokrs with our customer user model
    """

    def create_user(self, email, name, password=None):
        """
        Create a user profile object
        :param email:
        :param name:
        :param password:
        :return:
        """

        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """
        Create and save a new superuser
        :param email:
        :param name:
        :param password:
        :return:
        """

        user = self.create_user(email, name, password)

        user.is_superuser = True

        user.is_staff = True

        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
        Represent a user profile inside our system.
    """

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """
            Used to get a user full name
        """

        return self.name

    def get_short_name(self):
        """
            Used to get a user short name
        :return:
        """

        return self.name

    def __str__(self):
        """
            Django uses this to convert the object to string
        :return:
        """

        return self.email


class ProfilFeedItem(models.Model):
    """Profile status update."""

    user_profile = models.ForeignKey('UserProfile', on_delete=models.CASCADE)
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return the model as a string"""

        return self.status_text