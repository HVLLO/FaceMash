from rest_framework import routers

from .views import PostAPIViewSet


# register router
router = routers.DefaultRouter()
router.register('post', PostAPIViewSet, base_name='post_router')

urlpatterns = router.urls
