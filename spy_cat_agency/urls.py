from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CatViewSet, MissionViewSet, TargetViewSet

router = DefaultRouter()
router.register(r'cats', CatViewSet)
router.register(r'missions', MissionViewSet)
router.register(r'targets', TargetViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('missions/<int:pk>/assign-cat/', MissionViewSet.as_view({'post': 'assign_cat'}), name='assign-cat'),
    path('targets/<int:pk>/', TargetViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='target-detail'),
    path('targets/<int:pk>/complete/', TargetViewSet.as_view({'post': 'mark_complete'}), name='mark-target-complete'), 
]