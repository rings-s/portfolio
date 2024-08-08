from django.db import models
from django.contrib.auth.models import User

class Client(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)
    profile_image = models.ImageField(upload_to='client_images/')

    def __str__(self):
        full_name = self.user.get_full_name()
        return full_name if full_name else self.user.username
    
    
class Service(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    file = models.FileField(upload_to='project_files/')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    logo_img = models.ImageField(upload_to='project_logos/')
    end_date = models.DateField()
    service_tag = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='testimonial_images/')
    project_name = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    testimonial_body = models.TextField()

    def __str__(self):
        return f"{self.client_name} - {self.project_name}"
