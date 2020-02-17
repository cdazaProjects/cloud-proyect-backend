from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ContestListCreateView, ContestDetailView, VideoListCreateView, VideoDetailView, ContestDetailByURLView

urlpatterns = [
    path("contest",ContestListCreateView.as_view()),
    path(r'^public/contest/$',ContestDetailByURLView.as_view()),
    path("contest/<int:pk>", ContestDetailView.as_view()),
    path("video",VideoListCreateView.as_view()),
    path("videoContest/<int:pk>",VideoListCreateView.as_view()),
    path("video/<int:pk>",VideoDetailView.as_view()),
]
