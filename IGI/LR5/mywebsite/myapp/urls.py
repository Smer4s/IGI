from django.urls import path
from . import views

urlpatterns = [
    path('', views.mainpage),
    path('about/', views.aboutpage),
    path('faq/', views.faqpage),
    path('news/', views.newspage),
    path('contacts/', views.contactpage),
    path('confidential/',views.confidentialpage),
    path('employees/', views.employeepage),
    path('discounts/', views.discountpage),
    path('reviews/', views.reviewpage),
    path('reviews/add/', views.addreview),
    path('login/', views.loginpage),
    path('login/loginuser/', views.login_action),
    path('register/', views.registerpage),
    path('register/registeruser/', views.register_action),
    path('account/', views.accountpage),
    path('account/logout/', views.logout_action),
    path('schedule/', views.schedulepage),
    path('services/', views.servicepage),
    path('visits/', views.visitspage)
]