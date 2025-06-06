from django.urls import path
from . import views

app_name = 'offerings'

urlpatterns = [
    path('', views.offering_list, name='list'),
    path('create/', views.offering_create, name='create'),
    path('<int:pk>/update/', views.offering_update, name='update'),
    path('<int:pk>/delete/', views.offering_delete, name='delete'),
] 