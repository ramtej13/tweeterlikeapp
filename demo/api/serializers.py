from rest_framework import serializers

from django.contrib.auth import authenticate

from demo.models import test, PetsDetails, Pets

class testSerializer(serializers.ModelSerializer):
    class Meta:
        model = test
        fields = ("titel","discription")

class petsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetsDetails
        fields = ("pet_Name","pet_address","pet_colour","pet_bread")

class UserDetails(serializers.ModelSerializer):
    class Meta:
        model = Pets
        fields = ("petUser","pet_details")

