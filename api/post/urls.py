from rest_framework import routers

from .views import PostAPIViewSet


# register router
router = routers.DefaultRouter()
router.register('post', PostAPIViewSet, base_name='post_router')

urlpatterns = router.urls


"""
curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6Imh2bGxvd2UzbkBnbWFpbC5jb20iLCJleHAiOjE1NDUzNzQ5NzUsImVtYWlsIjoiaHZsbG93ZTNuQGdtYWlsLmNvbSJ9.TWMCK1l8GycuFTnT0joBRuql2objBk2k8vGdRvH1mk0" http://localhost:8000/api/v1/post/  
"""
