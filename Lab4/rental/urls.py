from django.urls import path
from .views import FriendViewset, BelongingViewset, BorrowedViewset
from rest_framework.routers import SimpleRouter

# from .views import UserList, UserDetail, PostList, PostDetail



# urlpatterns = [
    # path('users/', UserList.as_view()),
    # path('users/<int:pk>/', UserDetail.as_view()), 

    # path('<int:pk>/', PostDetail.as_view()),
    # path('', PostList.as_view()),

# ]
# router zastępuje urlpatterns
router = SimpleRouter()
router.register('', FriendViewset, basename='friendset')
router.register('', BelongingViewset, basename='belongingset')
router.register('', BorrowedViewset, basename='borrowedset')
urlpatterns = router.urls