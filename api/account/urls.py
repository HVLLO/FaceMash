from django.urls import path

from api.account.REST_API import views

urlpatterns = [
    path('create/', views.CreateUserAPIView.as_view(), name='create_user'),
]
