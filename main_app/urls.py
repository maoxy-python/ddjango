
from django.urls import path
from . import views
urlpatterns = [
    path('tt/',views.IndexView.as_view()),
]