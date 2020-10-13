from django.urls import path, include
from organizer.apis.commons import views
from rest_framework.routers import DefaultRouter


app_name = "organizer"

router = DefaultRouter()

router.register(r"organizers", views.TagViewSet)

urlpatterns = [
    path('', include(router.urls)),
    ]
