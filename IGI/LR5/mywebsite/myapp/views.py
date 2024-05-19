from django.shortcuts import render, redirect
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required,permission_required
from django.http import JsonResponse,HttpRequest
from datetime import datetime
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .models import (About, Question, Article, 
Contact, Employee, Discount, Review, Schedule, Client, PlannedVisit)

# Create your views here.
def mainpage(request):
    data = {'user':request.user}
    return render(request, 'index.html', data)

def aboutpage(request):
    about = About.objects.first()
    data = {'name':about.companyname, 'about':about.about_text}
    return render(request, 'about.html', data)

def faqpage(request):
    questions = Question.objects.all()
    data = {'questions':questions}
    return render(request, 'faq.html',data)

def newspage(request):
    news = Article.objects.all()
    data = {'news':news}
    return render(request, 'news.html', data)

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
     
    return redirect('/myapp/reviews')

def loginpage(request):
    return render(request, 'login.html')

def login_action(request):
    username = request.POST['login']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/myapp')
    else:
        messages.error(request, 'Неверный логин или пароль. Пожалуйста, попробуйте снова.')
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
    
    return redirect('/myapp')

@login_required(redirect_field_name='/myapp/')
def accountpage(request):
    user_group = request.user.groups.get()
    
    if user_group.name != 'Doctor':
        template = 'account_client.html'
    else:
        template = 'account_doctor.html'    
        
    return render(request, template, {'user': request.user})    

@login_required
def logout_action(request):
    logout(request)
    return redirect('/myapp/')

def visitspage(request:HttpRequest):
    data = {'visits': PlannedVisit.objects.all()}

    return render(request, 'visits.html', data)

@permission_required('myapp.view_schedule', login_url='/myapp/login')
def schedulepage(request:HttpRequest):    
    return render(request, 'schedule.html', {'schedules': Schedule.objects.all()})

def servicepage(request):
    pass