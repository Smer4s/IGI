import os

from typing import Any
from decimal import Decimal
import logging
import numpy as np
import matplotlib.pyplot as plt
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views import generic
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpRequest
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.mixins import LoginRequiredMixin

from django.conf import settings
from .models import (About, Question, Article, 
Contact, Employee, Discount, Review, Schedule, 
Client, PlannedVisit, Category, Service, Sale, Cart,
Partner)

# Create your views here.
def allpage(request):
    return render(request, 'all_tags.html')

def mainpage(request):
    article = Article.objects.first()
    
    services = Service.objects.all()
    partners = Partner.objects.all()
    
    ad_pictures = [os.path.join('company', 'ads', f) for f in os.listdir(os.path.join(settings.BASE_DIR,'static','company','ads'))]
    
    data = {
        'user': request.user, 
        'article': article,
        'ads': ad_pictures,
        'services':services,
        'partners':partners,
    }
    return render(request, 'index.html', data)

def aboutpage(request):
    about = About.objects.first()
    data = {'about':about }
    about.about_text
    return render(request, 'about.html', data)

def faqpage(request):
    questions = Question.objects.all()
    data = {'questions':questions}
    return render(request, 'faq.html',data)

def newspage(request):
    news = Article.objects.all()
    data = {'news':news}
    return render(request, 'news.html', data)

def newpage(request:HttpRequest, id:int):
    new = Article.objects.get(id=id)
    data = {'new':new}
    return render(request, 'new.html', data)

def contactpage(request):
    contacts = Contact.objects.all()
    data = {'contacts': contacts}
    return render(request, 'contacts.html', data)

def confidentialpage(request):
    return render(request, 'confidential.html')

def employeepage(request):
    employees = Employee.objects.all()
    data = {'employees': employees}
    return render(request, 'employees.html', data)

def discountpage(request):
    discounts = Discount.objects.all()
    data = {'discounts': discounts}
    return render(request, 'discounts.html', data)

def reviewpage(request):
    reviews = Review.objects.all()
    data = {'reviews': reviews, 'user': request.user}
    return render(request, 'reviews.html', data)

@login_required
def addreview(request):
    text = request.POST['text']
    mark = request.POST['mark']
    username = request.user.get_username()
    date = datetime.now()
    
    mark = int(mark)
    if mark > 10:
            mark = 10
    elif mark < 1:
            mark = 1
    
    Review.objects.create(issuer_name=username, mark=mark, review_date=date, text=text)
     
    logging.info(date.strftime('%d/%m/%Y, %H:%M:%S') +' user: ' + username + ' added a review with text: ' + text)
     
    return redirect('/myapp/reviews')

def loginpage(request):
    return render(request, 'login.html')

def login_action(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    logging.info('user authenthicated: ' + username)
    if user is not None:
        login(request, user)
        return redirect('/myapp/account')
    else:
        messages.error(request, 
'Неверный логин или пароль. Пожалуйста, попробуйте снова.')
        return redirect('/myapp/login')

def registerpage(request):
    return render(request, 'register.html')

def register_action(request:HttpRequest):
    username = request.POST['login']
    password = request.POST['password']
    email = request.POST['email']
    role = request.POST['role']
    
    user = User.objects.create_user(username=username, password=password, email=email)
    
    group = Group.objects.get(name=role) 
        
    group.user_set.add(user)
    
    logging.info('user registered: ' + username)
    
    return redirect('/myapp/account')

@login_required(redirect_field_name='/myapp/')
def accountpage(request):
    user_group = request.user.groups.get()

    data = {'user': request.user, 'categories' : Category.objects.all()}
    if user_group.name != 'Doctor':
        template = 'account_client.html'
    else:
        template = 'account_doctor.html'  
        try:
            doctor = Contact.objects.get(mail=request.user.email)
            data.update({'is_doctor': doctor})
        except Contact.DoesNotExist:
            logging.error('cannot find a group doctor for user: ' + request.user.get_username)
        
    return render(request, template, data)    

def addcontact(request):
    name = request.POST['name']
    telephone = request.POST['telephone']
    work_type = request.POST['work-type']
    
    category = Category.objects.get(name=work_type)
    
    Contact.objects.create(mail=request.user.email,name=name, phone=telephone,work_type=category)
    
    return redirect('/myapp/account/')

@login_required
def logout_action(request):
    logout(request)
    return redirect('/myapp/')

@login_required
def visitspage(request:HttpRequest):
    doctor = Contact.objects.get(mail=request.user.email)
    
    data = {'visits': PlannedVisit.objects.filter(doctor=doctor)}

    return render(request, 'visits.html', data)

@permission_required('myapp.view_schedule', login_url='/myapp/login')
def schedulepage(request):    
    return render(request, 'schedule.html', {'schedules': Schedule.objects.all()})

class ServiceView(generic.ListView, LoginRequiredMixin):
    model = Service
    context_object_name = 'services'
    template_name = 'services.html'
    
    def get_queryset(self) -> QuerySet[Any]:
        return Service.objects.all()

def addservice(request:HttpRequest):
    if request.method == 'POST':
        price = request.POST.get('price')
        name = request.POST.get('name')
        service = Service(price=price,name=name)
        service.save()
        
    return redirect('/myapp/services')

def view_service(request:HttpRequest, id:int):
    service = Service.objects.get(id=id)
    
    data = {
        'service' : service
    }
    
    return render(request, 'service.html', data)

@login_required
def add_to_cart(request:HttpRequest):
    if request.method == 'POST':
        id = request.POST['service-id']
        service = Service.objects.filter(id=id).first()
        client = Client.objects.filter(email=request.user.email).first()
        if client == None:
            return redirect("/myapp/login")
        
        cart = Cart.objects.filter(client=client).first()
    
        if cart == None:
            cart = Cart.objects.create(client=client, total_cost=0, promo_code=Discount.objects.first())
        
        cart.services.add(service)
        cart.save()
        
        return redirect('/myapp/buy')
        

def editservice(request:HttpRequest, id:int):
    service = Service.objects.get(id=id)
    
    if request.method == 'POST':
        service.name = request.POST['name']
        service.price = request.POST['price']
        service.save()
        return redirect('/myapp/services')
    
    return render(request,'editservice.html',{'service':service})

def deleteservice(request:HttpRequest, id:int):
    service = Service.objects.get(id=id)
    service.delete()
    
    return redirect('/myapp/services')

@login_required
def salespage(request):
    user_group = request.user.groups.get()
    
    if user_group.name == 'Doctor':
        template = 'sales.html'
        doctor = Contact.objects.get(mail=request.user.email)   
        if doctor == None:
            return redirect("/myapp/login") 
        sales = Sale.objects.filter(client__doctor=doctor)
        sum = 0
        for sale in sales:
            sum += sale.service.price 
                
        data = {'sales':sales, 'sum': sum}
        
    else:
        template='sales_client.html'
        client = Client.objects.filter(email=request.user.email).first()
        if client == None:
            return redirect("/myapp/login")
        
        cart = Cart.objects.filter(client=client).first()
        show = cart == None or cart.services == []
        services = []
        if cart != None:
            services = cart.services.all()
        
        data={'cart': cart, 'services':services, 'show':show}

     
    return render(request, template, data)


@login_required
def buypage(request):
    client = Client.objects.filter(email=request.user.email).first()
    if client == None:
        return redirect("/myapp/login")

    cart = Cart.objects.filter(client=client).first()
    no_cart = cart == None
    services = Service.objects.all()  
    codes = Discount.objects.all()  

    selected_services = cart.services.values_list('name', flat=True) if not no_cart else []
        
    data = {
        'services': services,
        'codes': codes,
        'selected_services': selected_services,  
    }
    return render(request,'buy.html', data)
    
@login_required
def purchase_action(request:HttpRequest):    
    return redirect('/myapp/webpay')
    
@login_required
def webpay(request:HttpRequest):    
    return render(request, 'webpay.html')

@login_required
def purchased(request:HttpRequest):
    client = Client.objects.get(email=request.user.email)
    cart = Cart.objects.get(client=client)
    
    cart.delete()
    return render(request, 'purchased.html')
    
@login_required   
def buy_action(request:HttpRequest):
    client = Client.objects.get(email=request.user.email)
    service_names = request.POST.getlist('service_name')
    
    code = request.POST['promo_code']
    discount = Discount.objects.get(code=code)
    
    print(discount.code)

    cart = Cart.objects.filter(client=client).first()
    
    if cart == None:
        cart = Cart.objects.create(client=client, total_cost=0, promo_code=discount)

    services = Service.objects.filter(name__in=service_names)

    service_dict = {service.name: service for service in services}

    if service_names == []:  
        cart.delete()
        return redirect('/myapp/sales')    
    
    total_cost = Decimal(0)
    for service in services:              
        total_cost += Decimal(service.price)   
        
        if Sale.objects.filter(client=client, service=service).exists():
            continue
               
        Sale.objects.create(client=client, service=service, date=datetime.now())

    dicount_percent = Decimal(1 - discount.value * 0.01)
    
    total_cost *= dicount_percent


    cart.total_cost = total_cost  
    cart.services.set(services) 
    cart.save()
    
    return redirect('/myapp/sales')

@login_required
def statspage(request:HttpRequest):
    prices = Sale.objects.all().values_list('service__price', flat=True)
    service_ids = Sale.objects.all().values_list('service__id', flat=True)  
    
    total_cost = sum(prices)
    average_cost = np.mean(prices)
    median_cost = np.median(prices)
    
    x_values = service_ids
    y_values = prices
    
    plt.figure(figsize=(10, 6))
    plt.plot(x_values, y_values, 'o-', label='Prices per Service', color='blue')  
    plt.axhline(y=average_cost, color='red', linestyle='--', label='Average Cost')
    plt.axhline(y=median_cost, color='green', linestyle='-.', label='Median Cost')
  #  plt.axhline(y=total_cost, color='blue', linestyle='solid', label='Total')
    
    plt.xlabel('Service ID')
    plt.ylabel('Price')
    plt.title('Prices per Service')
    plt.legend()
    
    filename = 'graph.png'
    
    graph_url = os.path.join(settings.BASE_DIR, 'static', filename)
   
    plt.savefig(graph_url)
    
    clients = Client.objects.all().order_by('name')
    
    data = {
        'total': total_cost,
        'average': average_cost,
        'median': median_cost,
        'clients': clients,
        'filename': filename
    }
    
    return render(request, 'stats.html', data)

