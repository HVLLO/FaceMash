from rest_framework import routers

from api.post.REST_API.views import PostAPIViewSet


# register router
router = routers.DefaultRouter()
router.register('post', PostAPIViewSet, base_name='post_router')

urlpatterns = router.urls
