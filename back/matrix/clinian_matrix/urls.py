from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'nurses', NurseViewSet, basename='nurses')
router.register(r'managers', ManagerViewSet, basename='managers')
router.register(r'skills', SkillViewSet, basename='skills')

urlpatterns = router.urls