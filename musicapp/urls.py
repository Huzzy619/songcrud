from django.urls import path
from .views import ArtisteView, SongViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register("song", SongViewSet)

urlpatterns = [
    
    path("artiste", ArtisteView.as_view()),
    # path("test", test)


] + router.urls
