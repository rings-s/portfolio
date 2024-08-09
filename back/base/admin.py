from django.contrib import admin
from .models import Client, Project, Testimonial, Blog, Contact



@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('name__username', 'phone_number')  # Searching through the User's username

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'client', 'created_at', 'end_date')
    list_filter = ('created_at', 'end_date', 'client')
    search_fields = ('name', 'description', 'client__name__username')
    raw_id_fields = ('client',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'project_name', 'date')
    list_filter = ('date',)
    search_fields = ('client_name', 'project_name', 'testimonial_body')

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('title', 'description')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email', 'message')

