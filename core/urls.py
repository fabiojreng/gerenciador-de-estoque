from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.home, name="home"),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("", include("brands.urls")),
    path("", include("categories.urls")),
    path("", include("suppliers.urls")),
    path("", include("inflows.urls")),
    path("", include("outflows.urls")),
    path("", include("products.urls")),
]
