from django.forms import widgets
from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id', 'title', 'code', 'lineos', 'language', 'style')