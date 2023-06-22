from rest_framework import serializers
from .models import BloodDonor


class BloodDonorSerializer(serializers.ModelSerializer):
    class Meta:
        model =BloodDonor
        fields='__all__'
