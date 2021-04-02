"""Define URLS for application poll."""
from django.conf.urls import url
from django.urls import path, include

from . import views

urlpatterns = [
    # login token
    path('login/', views.login, name='login'),
    # poll url
    path('poll/all/', views.poll_list_all, name='poll_all'),
    path('poll/all_active/', views.poll_list_active, name='poll_active'),
    path('poll/update/<int:poll_id>', views.delete_or_update_poll, name='poll_update'),
]
