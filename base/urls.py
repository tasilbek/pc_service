from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('pricing/', PricingPageView.as_view(), name='pricing'),
    path('service/', ServicePageView.as_view(), name='service'),
    path('service_detail/', ServiceDetailPageView.as_view(), name='service_detail'),
    path('blog/', views.blogPageView, name='blog'),
    path('blog_detail/<int:pk>', views.blogDetail, name='blog_detail'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('yuridik_shaxslar/', YuridikPersonPageView.as_view(), name='yuridik-shaxslar'),
    path('jismoniy_shaxslar/', JismoniyPersonPageView.as_view(), name='jismoniy-shaxslar')
]