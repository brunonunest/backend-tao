from django.urls import path, include
from accounts.apis.auth import views
from rest_framework.routers import DefaultRouter

app_name = "accounts"

router = DefaultRouter()

#router.register(r"login", views.LoginViewSet),

urlpatterns = [
    path('', include(router.urls)),
    ]
