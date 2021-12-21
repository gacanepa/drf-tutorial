from django.urls import path, include
from rest_framework.routers import DefaultRouter
from snippets.views import SnippetViewSet, UserViewSet

# Create a router and register the viewsets with it
router = DefaultRouter()

# The first argument is the URL preffix and the second is the viewset
router.register(r"snippets", SnippetViewSet)
router.register(r"users", UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
