from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import CustomerListCreateView, CustomerDetailView, ContestListCreateView, ContestDetailView, VideoListCreateView, VideoDetailView

urlpatterns = [
    path("customer",CustomerListCreateView.as_view()),
    path("customer/<int:pk>",CustomerDetailView.as_view()),

    path("contest",ContestListCreateView.as_view()),
    path("contest/<int:pk>",ContestDetailView.as_view()),
    
    path("video",VideoListCreateView.as_view()),
    path("video/<int:pk>",VideoDetailView.as_view()),
]
