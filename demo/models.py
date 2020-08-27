from django.db import models
import random
import time
from django.conf import settings

User = settings.AUTH_USER_MODEL

class test(models.Model):
    titel = models.CharField(max_length=100,default="hello"+str(round(time.time())))
    discription = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.titel

pet_bread_choices = (
    ("1", "lab"),
    ("2", "golden"),
    ("3", "lasiposo"),
    ("4", "dabor"),
    ("5", "raj"),
    ("6", "policec"),
    ("7", "pug"),
    ("8", "seslo"),
)
petc_colour_choices = (
    ("1", "black"),
    ("2", "gray"),
    ("3", "white"),
    ("4", "brown"),
)

class PetsDetails(models.Model):
    petID = models.CharField(max_length=100,default="pet_"+str(str(time.time()).replace(".","")))
    pet_Name = models.CharField(max_length=100)
    pet_address = models.TextField()
    pet_colour = models.TextField(max_length=200,choices=petc_colour_choices)
    pet_bread = models.CharField(max_length=100,choices=pet_bread_choices)

    def __str__(self):
        return self.petID

class Pets(models.Model):
    petUser = models.ForeignKey(User,on_delete=models.CASCADE)
    pet_details = models.OneToOneField(PetsDetails,on_delete=models.CASCADE,blank=True)

    # def __str__(self):
        # return self.pet_details