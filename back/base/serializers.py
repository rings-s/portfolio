from rest_framework import serializers
from .models import Client, Project, Testimonial, Blog, Contact
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "first_name", "last_name", "email"]

class ClientSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Client
        fields = [
            "user",
            "phone_number",
            "email",
            "created_at",
            "profile_image",
        ]
        read_only_fields = ("created_at",)

class ProjectSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    logo = serializers.ImageField(use_url=True)

    class Meta:
        model = Project
        fields = [
            "name",
            "description",
            "created_at",
            "file",
            "client",
            "logo",
            "end_date",
        ]
        read_only_fields = ("created_at",)

class TestimonialSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    project = ProjectSerializer(read_only=True)

    class Meta:
        model = Testimonial
        fields = [
            "client",
            "project",
            "date",
            "testimonial_body",
        ]
        read_only_fields = ("date",)

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ["title", "description", "image", "created_at"]
        read_only_fields = ("created_at",)

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ["name", "email", "message"]
