from django.urls import path
from . import views
from .views import HomePageView, AccountSettingsView, MySpotsView, BusinessDetailsView, ReviewView, add_marker

urlpatterns = [
    path('', HomePageView.as_view(), name='Home'),
    path('Account_settings/', AccountSettingsView.as_view(), name='Account_settings'),
    path('My_spots/', MySpotsView.as_view(), name='My_spots'),
    path('business/<int:business_id>/', BusinessDetailsView.as_view(), name='business_details'),
    path('profile/<int:user_id>/', views.UserProfileView.as_view(), name='user_profiles'),
    path('business/<int:business_id>/reviews/', ReviewView.as_view(), name='business_reviews'),
    path('markers/', add_marker)
    # Add other URL patterns as needed
]