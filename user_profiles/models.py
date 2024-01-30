from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Your CustomUser model fields
    profile_picture = models.ImageField(upload_to='profile_pics', blank=True)
    bio = models.TextField(max_length=500, blank=True)

    groups = models.ManyToManyField(
        "auth.Group",
        verbose_name="Groups",
        blank=True,
        related_name="custom_user_groups"
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        verbose_name="User permissions",
        blank=True,
        related_name="custom_user_permissions"
    )


class Review(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    business = models.CharField(max_length=100)  # For example
    # Add other fields for the review: text, rating, timestamp, etc.
    # Example:
    text = models.TextField()
    rating = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
