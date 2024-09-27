from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator

class Review(models.Model):
    issuer_name = models.CharField(max_length=30)
    mark = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(10)
        ])
    text = models.CharField(max_length=100)
    review_date = models.DateField(default=None)

class Discount(models.Model):
    code = models.CharField(max_length=10)
    value = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(100)
        ])
    is_active = models.BooleanField()
    
class Partner(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)
    site_url = models.URLField(max_length=200,
                               default="https://doctorface.by/")
    image_url = models.URLField(max_length=200,
                                default="https://doctorface.by/upload/CAllcorp3Medc/303/73auzuayw1hh7elpf74bmd9nh8lu14jo.png")

class Employee(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=50)

class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.CharField(max_length=17)
    mail = models.CharField(max_length=30)
    work_type = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='doctors')
    image_url = models.CharField(
        max_length=500,
        default='https://devscience.by/assets/img/team/team-3.jpg'
        )

class Article(models.Model):
    title = models.CharField(max_length=30)
    text = models.CharField(max_length=100)
    image_url = models.CharField(
        max_length=500,
        default='https://smaller-pictures.appspot.com/images/dreamstime_xxl_65780868_small.jpg'
        )

class Question(models.Model):
    question_text = models.CharField(max_length=100)
    answer_text = models.CharField(max_length=100)
    answer_date = models.DateField()

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    inn = models.CharField(max_length=12) 
    registry_number = models.CharField(max_length=4)
    email = models.EmailField(max_length=100) 
    address = models.TextField(blank=True) 
    phone = models.TextField(blank=True)
    website_url = models.URLField(max_length=200, null=True)
    print_url = models.URLField(max_length=200, null=True)

    def __str__(self):
        return self.title

class About(models.Model):
    companyname = models.CharField(max_length=30)
    about_text = models.CharField(max_length=300)
    video_url = models.URLField(max_length=200, blank=True)  
    logo = models.URLField(max_length=200, blank=True)  
    history = models.TextField(blank=True)  
    details = models.TextField(blank=True)  
    certificate = models.OneToOneField(Certificate, on_delete=models.CASCADE, blank=True, null=True) 
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    doctor = models.OneToOneField(Contact, on_delete=models.CASCADE, related_name='client', null=True)

class Room(models.Model):
    number = models.IntegerField()

class Service(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    clients = models.ManyToManyField(Client, through='Sale')

class Cart(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    services = models.ManyToManyField(Service)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)
    promo_code = models.ForeignKey(Discount, on_delete=models.CASCADE)

class Sale(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    date = models.DateField()

class Schedule(models.Model):
    doctor = models.ForeignKey(Contact, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    day = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()

class PlannedVisit(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Contact, on_delete=models.CASCADE)
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    visit_date = models.DateField()
