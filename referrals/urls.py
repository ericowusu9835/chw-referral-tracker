from django.urls import path
from . import views

urlpatterns = [
    path('', views.tracker_view, name='tracker'),
    path('tracker/', views.tracker_view, name='tracker_page'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('home/', views.home, name='home'),
    path('send-sms/<int:referral_id>/', views.send_sms_view, name='send_sms'),
]