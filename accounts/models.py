from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    USER_TYPE_SEEKER = 'seeker'
    USER_TYPE_EMPLOYER = 'employer'
    USER_TYPE_CHOICES = [
        (USER_TYPE_SEEKER, 'Job Seeker'),
        (USER_TYPE_EMPLOYER, 'Employer'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES, default=USER_TYPE_SEEKER)
    phone = models.CharField(max_length=15, blank=True)
    company_name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username} ({self.get_user_type_display()})'

    @property
    def is_employer(self):
        return self.user_type == self.USER_TYPE_EMPLOYER

    @property
    def is_seeker(self):
        return self.user_type == self.USER_TYPE_SEEKER
