from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('task/<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('register/', views.create_user_form, name='create_user'),
    path('accounts/profile/', views.ProfileView.as_view(), name='profile'),
    path('create_task/', views.create_task, name='create_task'),
    path('change_task/<int:pk>', views.change_task, name='change_task'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
]