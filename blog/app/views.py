from django.shortcuts import render, R
from django.contrib.auth.models import User
from app.serializers import BlogSerializer
from app.models import Blog
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework import renderers


class BlogList(viewsets.ViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    parser_classes = IsAuthenticated
    

    @action(detail = True, renderer_classes= [renderers.StaticHTMLRenderer])
    def highlight(self, request , *args, **kwargs):
        blog = self.get_object()
        return Response(blog.highlight)
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




