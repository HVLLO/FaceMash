from django.urls import path

from . import views


urlpatterns = [
    path('create/user/', views.CreateUserAPIView.as_view()),
    path('obtain/token/', views.auth_user),
    path('create/post/', views.CreatePostAPIView.as_view()),
    path('update/post/', views.UpdatePostAPIView.as_view()),
    path('list/post/', views.ListPostAPIView.as_view()),
    path('detail/post/<int:pk>/', views.DetailPostAPIView.as_view()),
]
