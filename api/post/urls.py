from django.urls import path

from . import views


urlpatterns = [
    path('create/', views.CreatePostAPIView.as_view()),
    path('update/', views.UpdatePostAPIView.as_view()),
    path('list/', views.ListPostAPIView.as_view()),
    path('detail/<int:pk>/', views.DetailPostAPIView.as_view()),
]
