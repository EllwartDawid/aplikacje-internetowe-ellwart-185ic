from django.urls import path
from .views import FriendViewset, BelongingViewset, BorrowedViewset, UserViewSet

from rest_framework.routers import SimpleRouter

# from .views import UserList, UserDetail, PostList, PostDetail



 #urlpatterns = [
    # path('users/', UserList.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()), 

    # path('<int:pk>/', PostDetail.as_view()),
    # path('', PostList.as_view()),

 #]
# router zastępuje urlpatterns
router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', FriendViewset, basename='friend')
router.register('belonging', BelongingViewset, basename='belonging')
router.register('borrowed', BorrowedViewset, basename='borrowed')
urlpatterns = router.urls