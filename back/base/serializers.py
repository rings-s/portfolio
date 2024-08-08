from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Service, Project, Testimonial

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Client
        fields = ['id', 'user', 'phone_number', 'created_at', 'profile_image']

class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'name']

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer()
    service_tag = ServiceSerializer()

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'created_at', 'file', 
            'client', 'logo_img', 'end_date', 'service_tag'
        ]

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id', 'client_name', 'client_image', 'project_name', 
            'date', 'testimonial_body'
        ]
