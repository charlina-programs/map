from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserProfileForm, ReviewForm
from .models import Review


@login_required
def view_profile(request):
    user_reviews = Review.objects.filter(user=request.user)
    return render(request, 'user_profiles/view_profile.html', {'user_reviews': user_reviews})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = UserProfileForm(instance=request.user)

    return render(request, 'user_profiles/edit_profile.html', {'form': form})


@login_required
def add_review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('view_profile')
    else:
        form = ReviewForm()

    return render(request, 'user_profiles/add_review.html', {'form': form})
