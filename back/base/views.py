from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import Client, Project, Testimonial, Blog, Contact #Service
from .serializers import ClientSerializer, ProjectSerializer,TestimonialSerializer, BlogSerializer, ContactSerializer  #ServiceSerializer



class ClientListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        clients = Client.objects.all()
        serializer = ClientSerializer(clients, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Client, pk=pk)

    def get(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientSerializer(client)
        return Response(serializer.data)

    def put(self, request, pk):
        client = self.get_object(pk)
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        client = self.get_object(pk)
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class ProjectListCreateView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Project, pk=pk)

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class TestimonialListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        testimonials = Testimonial.objects.all()
        serializer = TestimonialSerializer(testimonials, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TestimonialSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TestimonialDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Testimonial, pk=pk)

    def get(self, request, pk):
        testimonial = self.get_object(pk)
        serializer = TestimonialSerializer(testimonial)
        return Response(serializer.data)

    def put(self, request, pk):
        testimonial = self.get_object(pk)
        serializer = TestimonialSerializer(testimonial, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        testimonial = self.get_object(pk)
        testimonial.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class BlogListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class BlogDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(Testimonial, pk=pk)
    
    def get(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        blog = self.get_object(pk)
        serializer = BlogSerializer(blog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        blog = self.get_object(pk)
        blog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



    

    
class ContactListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get_object(self, pk):
        return get_object_or_404(Contact, pk=pk)
    
    def get(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact)
        return Response(serializer.data)
    
    
    def put(self, request, pk):
        contact = self.get_object(pk)
        serializer = ContactSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        contact = self.get_object(pk)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

        
    