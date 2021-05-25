from django.urls import path, include
from survey import views

app_name = 'polls'

urlpatterns = [
    path('login/', views.login, name='login'),
    path('poll/create_poll/', views.poll_create, name='create_poll'),
    path('poll/update_poll/<int:poll_id>/', views.poll_update, name='update_poll'),
    path('poll/view_poll/', views.polls_view, name='poll_view'),
    path('poll/view/active_pools/', views.active_polls_view, name='pool_active'),
    path('question/create_question/', views.question_create, name='create_question'),
    path('question/update_question/<int:question_id>/', views.question_update, name='update_question'),
    path('choice/create_choice/', views.choice_create, name='create_choice'),
    path('choice/update_choice/<int:choice_id>/', views.choice_update, name='update_choice'),
    path('answer/create_answer/', views.answer_create, name='create_answer'),
    path('answer/view_answer/<int:user_id>/', views.answer_view, name='view_answer'),
    path('answer/update_answer/<int:answer_id>/', views.answer_update, name='update_answer'),
]
