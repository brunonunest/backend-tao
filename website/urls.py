from django.urls import path, include
from website.commons import views
from rest_framework.routers import DefaultRouter


app_name = "website"

router = DefaultRouter()

router.register(r"posts", views.PostViewSet),

urlpatterns = [
    path('', include(router.urls)),
    ]
