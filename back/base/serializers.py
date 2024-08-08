from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Client, Project, Testimonial, Blog, Contact

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email']

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Ensure nested serialization does not expect writable input

    class Meta:
        model = Client
        fields = ['id', 'user', 'phone_number', 'created_at', 'profile_image']
        read_only_fields = ('created_at',)  # Ensure auto_now_add fields are read-only

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)  # Use read_only to avoid issues with nested writable serializer

    class Meta:
        model = Project
        fields = [
            'id', 'name', 'description', 'created_at', 'file', 
            'client', 'logo_img', 'end_date'
        ]
        read_only_fields = ('created_at',)  # Ensure auto_now_add fields are read-only

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = [
            'id', 'client_name', 'client_image', 'project_name', 
            'date', 'testimonial_body'
        ]
        read_only_fields = ('date',)  # Ensure auto_now_add fields are read-only

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'id', 'title', 'description', 'image', 'created_at'
        ]
        read_only_fields = ('created_at',)  # Ensure auto_now_add fields are read-only

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id', 'name', 'email', 'message'
        ]
