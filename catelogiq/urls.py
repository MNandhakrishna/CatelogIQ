"""catelogiq URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    path('', views.home, name='home'),
    path('log-analytics/', views.log_analytics, name='log_analytics'),
    path('analysis-options/', views.analysis_options, name='analysis_options'),
    path('anomaly-detection/', views.anomaly_detection, name='anomaly_detection'),
    path('stream-viewer/', views.stream_viewer, name='stream_viewer'),
    path('chatbot/', views.chatbot, name='chatbot'),
    path('dashboard/', views.databricks_dashboard_proxy, name='databricks_dashboard'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact, name='contact'),
    path('text-classification/', views.text_classification, name='text_classification'),
    path('debug_session/', views.debug_session, name='debug_session'),
    path('check_pipeline_status/', views.check_pipeline_status, name='check_pipeline_status'),
    path('reset_pipeline_status/', views.reset_pipeline_status, name='reset_pipeline_status'),
]
