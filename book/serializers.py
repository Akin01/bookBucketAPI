from rest_framework import serializers
from .models import bookList

class bookSerializer(serializers.ModelSerializer):
    class Meta:
        model = bookList
        fields = '__all__'
