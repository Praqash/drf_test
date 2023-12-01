from rest_framework import serializers
from app.models import Blog

class BlogSerializer(serializers.Serializer):
    class Meta():
        model = Blog
        fields = ["Title", "Author", "Content", "Created_at" ]