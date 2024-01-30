from django.urls import path
from .views import view_profile, edit_profile, add_review

urlpatterns = [
    path('view_profile/', view_profile, name='view_profile'),
    path('edit_profile/', edit_profile, name='edit_profile'),
    path('add_review/', add_review, name='add_review'),
]
