from rest_framework import serializers
from .models import CompaniesData

class CompaniesDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompaniesData
        fields = '__all__'
