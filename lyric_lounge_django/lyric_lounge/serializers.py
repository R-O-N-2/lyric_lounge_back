from rest_framework import serializers

from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    works = serializers.HyperlinkedRelatedField(
        view_name='work_detail',
        many=True,
        read_only=True
    )

    class Meta:
        model = User
        fields = ('id', 'name', 'photo_url', 'location', 'contact', 'password', 'works')


class AliasSerializer(serializers.HyperlinkedModelSerializer):
    works = serializers.HyperlinkedRelatedField(
        view_name='work_detail',
        read_only=True,
        many=True
    )
    class Meta: 
        model = Alias 
        fields = ('id','name', 'works')


class WorkSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name='user_detail',
        read_only=True
    )
    genre = serializers.HyperlinkedRelatedField(
        view_name='genre_detail',
        read_only=True
    )
    class Meta:
        model = Work
        fields = ('id', 'user', 'title', 'content', 'likes', 'genre')


class GenreSerializer(serializers.HyperlinkedModelSerializer):
   
    class Meta:
        model = Genre
        fields = ('id', 'name')

