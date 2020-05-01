from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home),
    # path('update_classic/', views.update_classic),
    re_path(r'_+(.+)', views.details),
    # path('update/', views.update),
]