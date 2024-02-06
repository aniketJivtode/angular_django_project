from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone


class User_Management(AbstractUser):
    username = models.CharField(max_length=30, blank=True)
    email = models.EmailField(max_length=100, unique=True)
    user_type = models.IntegerField(null=True, blank=True)
    # full_name = models.CharField(max_length=255)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    department = models.CharField(max_length=255, null=True, blank=True)
    password_expiry_status = models.CharField(max_length=255, null=True, blank=True)
    password_change_attempts = models.IntegerField(null=True, blank=True)
    user_status = models.IntegerField(null=True, blank=True)
    password_creation_date = models.CharField(max_length=255, null=True, blank=True)
    password_creation_time = models.CharField(max_length=255, null=True, blank=True)
    rights = models.IntegerField(null=True, blank=True)
    visible = models.IntegerField(null=True, blank=True)
    created_on = models.DateTimeField(blank=True, null=True, editable=True)
    created_by = models.CharField(max_length=255, null=True, blank=True)
    modified_on = models.DateTimeField(blank=True, null=True, editable=True)
    modified_by = models.CharField(max_length=255, null=True, blank=True)
    remarks = models.CharField(max_length=255, null=True, blank=True)
    last_passwords = models.CharField(max_length=255, null=True, blank=True)
    server_rights = models.IntegerField(null=True, blank=True)
    server_visible = models.IntegerField(null=True, blank=True)
    server_access = models.IntegerField(null=True, blank=True)
    fingerprint_data1 = models.CharField(max_length=255, null=True, blank=True)
    fingerprint_data2 = models.CharField(max_length=255, null=True, blank=True)
    fingerprint_data3 = models.CharField(max_length=255, null=True, blank=True)
    fingerprint_data4 = models.CharField(max_length=255, null=True, blank=True)
    fingerprint_data5 = models.CharField(max_length=255, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'username']

    def save(self, *args, **kwargs):
        if not self.created_on and self._state.adding:
            self.created_on = timezone.now()
        self.modified_on = timezone.now()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    class Meta:
        db_table = 'user_management'
        # ordering = [
        #     'id', 'username', 'email', 'user_type', 'first_name', 'last_name', 'department',
        #     'password_expiry_status', 'password_change_attempts', 'user_status', 'password_creation_date',
        #     'password_creation_time', 'rights', 'visible', 'created_on', 'created_by', 'modified_on',
        #     'modified_by', 'remarks', 'last_passwords', 'server_rights', 'server_visible', 'server_access',
        #     'fingerprint_data1', 'fingerprint_data2', 'fingerprint_data3', 'fingerprint_data4',
        #     'fingerprint_data5', 'is_admin', 'is_active', 'is_staff', 'is_superuser'
        # ]
        ordering = ['-created_on']
