from django.db import models
from django.contrib.auth.models import User


class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Renamed from 'name' for clarity
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to="client_images/")

    def __str__(self):
        return self.user.username


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to="project_files/")
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, related_name="projects"
    )
    logo = models.ImageField(upload_to="project_logos/")
    end_date = models.DateField()

    def __str__(self):
        return self.name


class Testimonial(models.Model):
    client_name = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_name_testimonials")
    client_image = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="client_image_testimonials")

    project_name = models.ForeignKey(Project, on_delete=models.CASCADE, blank=True)

    date = models.DateTimeField(auto_now_add=True)
    testimonial_body = models.TextField()

    def __str__(self):
        return f"{self.client_name} - {self.project_name}"


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="blog_images/", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
