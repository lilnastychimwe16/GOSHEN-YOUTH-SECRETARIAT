from django.urls import path
from . import views

app_name = 'obligations'

urlpatterns = [
    path('zonal/', views.zonal_list, name='zonal_list'),
    path('zonal/create/', views.zonal_create, name='zonal_create'),
    path('zonal/<int:pk>/update/', views.zonal_update, name='zonal_update'),
    path('zonal/<int:pk>/delete/', views.zonal_delete, name='zonal_delete'),
    
    path('district/', views.district_list, name='district_list'),
    path('district/create/', views.district_create, name='district_create'),
    path('district/<int:pk>/update/', views.district_update, name='district_update'),
    path('district/<int:pk>/delete/', views.district_delete, name='district_delete'),
] 