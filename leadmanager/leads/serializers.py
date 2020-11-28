from django.db.models import fields
from rest_framework import serializers
from .models import Lead


class LeadSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'