from rest_framework import viewsets
from rest_framework_json_api.views import RelationshipView
from example.models import Blog, Entry, Author
from example.serializers import BlogSerializer, EntrySerializer, AuthorSerializer


class BlogViewSet(viewsets.ModelViewSet):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class EntryViewSet(viewsets.ModelViewSet):

    queryset = Entry.objects.all()
    serializer_class = EntrySerializer
    resource_name = 'posts'

class AuthorViewSet(viewsets.ModelViewSet):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer



class EntryRelationshipView(RelationshipView):
    queryset = Entry.objects

class BlogRelationshipView(RelationshipView):
    queryset = Blog.objects
