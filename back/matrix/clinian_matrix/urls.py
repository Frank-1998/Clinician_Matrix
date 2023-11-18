from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'nurses', NurseViewSet, basename='nurses')
router.register(r'managers', ManagerViewSet, basename='managers')
router.register(r'skills', SkillViewSet, basename='skills')
router.register(r'patients', PatientsViewSet, basename='patients')
router.register(r'certificates', CertificateViewSet, basename='certificates')
router.register(r'users', CustomUserViewSet, basename='users')

urlpatterns = router.urls