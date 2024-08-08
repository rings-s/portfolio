from django.urls import path
from .views import (
    ClientListCreateView, ClientDetailView,
    # ServiceListCreateView, ServiceDetailView,
    ProjectListCreateView, ProjectDetailView,
    TestimonialListCreateView, TestimonialDetailView,
    BlogListCreateView, BlogDetailView,
    ContactListCreateView, ContactDetailView
)

urlpatterns = [
    path('clients/', ClientListCreateView.as_view(), name='client-list-create'),
    path('clients/<int:pk>/', ClientDetailView.as_view(), name='client-detail'),
    # path('services/', ServiceListCreateView.as_view(), name='service-list-create'),
    # path('services/<int:pk>/', ServiceDetailView.as_view(), name='service-detail'),
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('testimonials/', TestimonialListCreateView.as_view(), name='testimonial-list-create'),
    path('testimonials/<int:pk>/', TestimonialDetailView.as_view(), name='testimonial-detail'),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('contacts/', ContactListCreateView.as_view(), name='contact-list-create'),
    path('contacts/<int:pk>/', ContactDetailView.as_view(), name='contact-detail')
]
