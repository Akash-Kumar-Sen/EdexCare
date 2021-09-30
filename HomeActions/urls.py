from django.urls import path
from . import views

urlpatterns = [
    path("all/<slug:name_slug>/", views.actions, name="actions"),
]