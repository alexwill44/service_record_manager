
from django.db import models
from django.db.models import Model, CharField, DateTimeField, ForeignKey
from django.db.models.deletion import SET_DEFAULT, SET_NULL
from django.db.models import IntegerField, TextField, ManyToManyField
from django.db.models.fields.related import ForeignKey, ForeignObject
# import auth_user_model for use in foreign key 
from django.contrib.auth.models import User
from django.urls.base import reverse


# Create your models here.

class Client(User): 
    address = CharField(max_length=500)
    phone = CharField(max_length=15)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name, self.last_name}"

class Tech(User): 
    rate = IntegerField(default=25)
    created_at = DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username}"

class Motorcycle(Model): 
    make = CharField(max_length=100)
    model = CharField(max_length=100)
    color = CharField(max_length=100)
    dom = CharField(max_length=8)
    vin = CharField(max_length=17)
    mileage = IntegerField(default=0)
    status = IntegerField(default=0)
    img = CharField(max_length=1000)
    created_at = DateTimeField(auto_now_add=True)
    owner = ForeignKey(User, on_delete=models.CASCADE, related_name='motorcycle')

    def __str__(self): 
        return f"{self.make}, {self.model}"

class Part(Model):
    part_number = CharField(max_length=100)
    description = TextField(max_length=1000)

    def __str__ (self):
        return f"{self.part_number}"

class Record(Model): 
    mileage = IntegerField(default=0)
    description = TextField(max_length=10000)
    created_at = DateTimeField(auto_now_add=True)
    motorcycle = ForeignKey(Motorcycle, on_delete=models.CASCADE, related_name='records')
    tech = ForeignKey(User, on_delete=SET_DEFAULT, default="No Technician Assigned", related_name='record')
    parts = ManyToManyField(Part) 

    def __str__ (self):
        return f"{self.motorcycle} by {self.tech.username}, 'at' {self.mileage} miles"

    class Meta:
        ordering = ['-created_at']



    





    