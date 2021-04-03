"""Define URLS for application poll."""
from django.urls import path

from . import views
from .yasg import urlpatterns as doc_url

urlpatterns = [
    # poll url
    path('poll/all/', views.poll_list_all, name='poll_all'),
    path('poll/all_active/', views.poll_list_active, name='poll_active'),
    path('poll/update/<int:poll_id>', views.delete_or_update_poll, name='poll_update'),
    path('poll/create/', views.create_poll, name='create_poll'),
    # question url
    path('question/create/', views.create_question, name='create_question'),
    path('question/update/<int:quest_id>', views.delete_or_update_question, name='update_question'),
    # choice url
    path('choice/create/', views.create_choice, name='create_choice'),
    path('choice/update/<int:choice_id>', views.delete_or_update_choice, name='choice_update'),
    # answer url
    path('answer/view/<int:user_id>', views.answer_view, name='view_answer'),
    path('answer/update/<int:answer_id>', views.delete_or_update_answer, name='answer_update'),
    path('answer/create/', views.answer_create, name='answer_create'),
    # voter
    path('voter/<int:user_id>', views.user_voter_view, name='user_voter_view'),
    path('voter/create/', views.user_voter_create, name='user_voter_create'),
    path('voter/delete/<int:user_id>', views.delete_user_voter, name='delete_user_voter'),
]

urlpatterns += doc_url
