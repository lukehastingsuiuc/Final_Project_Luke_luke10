# IMPORTS
from urllib import request
from django.shortcuts import render, get_object_or_404, redirect
from django.core.serializers import serialize
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from foodfinder.models import User, Restaurant, Review
from .forms import ReviewForm
from .forms_auth import UserSignUpForm
import requests
import json

class FoodBaseView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,'food/base.html', context={'restaurant_base_html': Restaurant.objects.all()})

class MapView(LoginRequiredMixin, View):
    def get(self, request):
        restaurants = Restaurant.objects.all()
        data = serialize('json', restaurants)
        context = {'model_data': data,
                   }
        return render(request, 'food/map_view.html', context)

class RestaurantView(LoginRequiredMixin, ListView):
    def post(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)
    model = Restaurant
    template_name = 'food/restaurant_list.html'
    context_object_name = 'restaurant_rows_for_looping'

class RestaurantDetailView(LoginRequiredMixin, DetailView):
    def get(self, request, primary_key):
        restaurant = get_object_or_404(Restaurant, pk=primary_key)
        reviews = restaurant.review_restaurant_name.all()
        return render(
            request,
            'food/restaurant_detail.html',
            {
                'single_restaurant_var_for_looping': restaurant,
                'reviews_var_for_looping': reviews,
            },
        )

class ReviewCreateView(LoginRequiredMixin, CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "food/new_review.html"
    success_url = reverse_lazy("restaurant-url")

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required(login_url='login_urlpattern')
def user_review(request):
    user_reviews = Review.objects.filter(user=request.user)
    context = {'reviews': user_reviews}
    return render(request, 'food/my_reviews.html', context)

def signup_view(request):
    if request.method == "POST":
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect("restaurant-url")
    else:
        form = UserSignUpForm()
    return render(request, "food/signup.html", {"form": form})



