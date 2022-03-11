from django.urls import path
from django.contrib.auth import views as auth_views
from asset_management_app import views
import asset_management_app
from asset_management_app.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset = LogMessage.objects.order_by("-log_date")[:5],
    context_object_name = "message_list",
    template_name = "asset_management_app/home.html",
)

urlpatterns = [
    path("", home_list_view, name="home"),
    path("log", views.log_message, name="log"),
    path("hello/<name>", views.hello_there, name="hello_there"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("accounts/profile/", views.ProflieView.as_view(), name="profile"),

    # Django Auth
    path("accounts/login", auth_views.LoginView.as_view(template_name="asset_management_app/accounts/login.html"), name="login"),
    path("accounts/logout", auth_views.LogoutView.as_view(), name="logout"),
]
