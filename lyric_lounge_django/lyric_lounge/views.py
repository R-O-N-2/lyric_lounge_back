# from django.shortcuts import render
# from .models import User
# from .models import Work

# # Create your views here.
# from django.http import JsonResponse

# # def UserList(request):
# #     users = User.objects.all().values('name', 'photo_url', 'location', 'contact') # only grab some attributes from our database, else we can't serialize it.
# #     users_list = list(users) # convert our artists to a list instead of QuerySet
# #     return JsonResponse(users_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.


# # def WorkList(request):
# #     works = Work.objects.all().values('user', 'title', 'content', 'likes') # only grab some attributes from our database, else we can't serialize it.
# #     works_list = list(works) # convert our artists to a list instead of QuerySet
# #     return JsonResponse(works_list, safe=False) # safe=False is needed if the first parameter is not a dictionary.


from rest_framework import generics
from .serializers import *
from .models import *

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class WorkList(generics.ListCreateAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class WorkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Work.objects.all()
    serializer_class = WorkSerializer

class GenreList(generics.ListCreateAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class GenreDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer

class AliasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer

class AliasList(generics.ListCreateAPIView):
    queryset = Alias.objects.all()
    serializer_class = AliasSerializer
