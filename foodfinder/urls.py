# IMPORTS
from . import views
from .views import FoodBaseView, RestaurantView, RestaurantDetailView, ReviewCreateView, MapView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

urlpatterns = [
    path('base', FoodBaseView.as_view(), name='food-base-url'),
    path('restaurant/', RestaurantView.as_view(), name='restaurant-url'),
    path('restaurant/<int:primary_key>/', RestaurantDetailView.as_view(), name='restaurant-detail-url'),
    path("restaurant/new-review/", ReviewCreateView.as_view(), name="add-review-url"),
    path("reviews/", views.user_review, name="my-reviews-url"),
    path("signup/", views.signup_view, name="signup_urlpattern"),
    path("login/", LoginView.as_view(template_name="food/login.html"), name="login_urlpattern"),
    path("logout/", LogoutView.as_view(next_page="login_urlpattern"), name="logout_urlpattern"),
    path("map/", MapView.as_view(), name="map_url"),
]