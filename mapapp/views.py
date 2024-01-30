import json

from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Business, Marker
from django.contrib.auth import get_user_model
from .models import Review
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods



from django.urls import path


# Create your views here.
CustomUser = get_user_model()


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        # Your view logic goes here
        return render(request, 'home.html')  # Adjust the template name as needed


class AccountSettingsView(View):
    def get(self, request, *args, **kwargs):
        # Add logic here to get user account settings
        return render(request, 'Account_settings.html')


class MySpotsView(View):
    def get(self, request, *args, **kwargs):
        # Add logic here to get user's spots
        return render(request, 'My_spots.html')


class BusinessDetailsView(View):
    template_name = 'business_details.html'

    def get(self, request, business_id, *args, **kwargs):
        try:
            business = get_object_or_404(Business, id=business_id)
        except Business.DoesNotExist:
            business = Business(name="Default Business", description="No details available")

        context = {
            'business': business,
            'business_picture': business.business_image,
            'business_description': business.description,
            'business_location': (business.location_lat, business.location_lon)
        }

        return render(request, self.template_name, context)


class ReviewView(View):
    template_name = 'reviews.html'

    def get(self, request, business_id, *args, **kwargs):
        business = get_object_or_404(Business, id=business_id)
        reviews = Review.objects.filter(business=business)

        context = {'business': business, 'reviews': reviews}
        return render(request, self.template_name, context)


class UserProfileView(View):
    template_name = 'user_profile.html'

    def get(self, request, user_id, *args, **kwargs):
        user = get_object_or_404(CustomUser, id=user_id)  # Change User to CustomUser
        # Logic to fetch user profile based on the user_id
        # Perform any necessary operations with the user object

        context = {'user': user}
        return render(request, self.template_name, context)

@csrf_exempt
@require_http_methods(["POST"])
def add_marker(request):
    ##Todo:validate request body

    body = json.loads(request.body.decode("UTF-8"))

    lat=body["lat"]
    lng=body["lng"]
    description=body["text"]
    Marker.objects.create(location_lat=lat, location_lon=lng, description=description)

    return HttpResponse()


