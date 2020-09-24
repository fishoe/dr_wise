from django.urls import path
from. import views

urlpatterns = [
    path('', views.first_page,name='home'),
    path('result/', views.result_page,name='result'),
]