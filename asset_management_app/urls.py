from django.urls import path
from asset_management_app import views

urlpatterns = [
    path("", views.home, name="home")
]
