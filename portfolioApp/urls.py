from django.urls import path
from .import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('ContactME/', views.ContactME, name="ContactME"),
    # path('cool/', views.cool, name="cool"),
]