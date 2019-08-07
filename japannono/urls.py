from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    # Create
    path('new/', views.new),
    path('create/', views.create),
    # path('delete/', views.delete),
]
