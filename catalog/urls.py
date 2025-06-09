from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log-analytics/', views.log_analytics, name='log_analytics'),
    path('analysis-options/', views.analysis_options, name='analysis_options'),
]