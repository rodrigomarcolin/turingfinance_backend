from django.contrib import admin
from django.urls import include, path
from tquant_api import views

urlpatterns = [
    path("histogram/", views.HistogramView.as_view()),
    path("rolling/", views.RollingView.as_view()),
]
