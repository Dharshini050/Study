from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudyViewSet, SubjectViewSet
from .views import LogFrontendMessages

router = DefaultRouter()
router.register('studies', StudyViewSet)
router.register('subjects', SubjectViewSet, basename='subject')

urlpatterns = [
    path('api/', include(router.urls)),
    path('log-frontend/', LogFrontendMessages.as_view(), name='log_frontend'),
]
