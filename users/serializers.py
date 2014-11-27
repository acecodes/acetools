from django.forms import widgets
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.Serializer):
	first_name = serializers.CharField(required=True, max_length=50)
	last_name = serializers.CharField(required=True, max_length=50)
	email = serializers.EmailField(required=True, max_length=50)
