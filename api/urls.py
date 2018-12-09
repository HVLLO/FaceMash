from django.urls import path

from . import views


urlpatterns = [
    path('create/user/', views.CreateUserAPIView.as_view()),
    path('obtain/token/', views.auth_user)
]
