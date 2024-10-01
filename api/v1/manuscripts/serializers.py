from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from accounts.models import User
from manuscripts.models import ManuscriptCategory, Manuscript


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ManuscriptCategory
        fields = ['id', 'title']


class ManuscriptCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Manuscript
        fields = ['title', 'category', 'file']


class ManuscriptListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manuscript
        fields = ['title', 'category', 'file', 'status']