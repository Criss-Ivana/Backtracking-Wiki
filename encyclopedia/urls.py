from django.urls import path
from . import views
app_name="pages"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>", views.wiki, name="wikipage"),
    path("Error/<str:error>", views.error, name="error")
]