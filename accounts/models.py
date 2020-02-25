from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_admin=False, is_staff=False):
        if not email:
            raise ValueError("Must have an E-mail")
        if not password:
            raise ValueError("Must have a password")

        user_obj = self.model(
            email=self.normalize_email(email)
        )

        user_obj.set_password(password)
        user_obj.is_active = is_active
        user_obj.is_staff = is_staff
        user_obj.is_admin = is_admin

        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, password=None):
        staffuser = self.create_user(email=email, password=password, is_staff=True)
        return staffuser

    def create_superuser(self, email, password=None):
        superuser = self.create_user(email=email, password=password, is_staff=True, is_admin=True)
        return superuser


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    is_active = models.BooleanField(default=True)  # Allowed to login
    is_staff = models.BooleanField(default=False)  # Staff user Not a SuperUser
    is_admin = models.BooleanField(default=False)  # Super User
    join_date = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'  # treated as default username
    REQUIRED_FIELDS = []  # username & password are required by default

    objects = UserManager()

    # My Custom User methods
    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    # Custom properties
