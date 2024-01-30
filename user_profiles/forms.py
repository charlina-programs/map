from django import forms
from .models import CustomUser, Review


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['bio', 'profile_picture']  # Add other fields as needed


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['business', 'rating', 'text']  # Add other fields as needed
