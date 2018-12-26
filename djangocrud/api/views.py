from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer,MovieSerializer
from .models import Movie


# from django.shortcuts import render
# from .models import Blog 
# from .serializers import BlogSerializer
# from rest_framework import viewsets


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer