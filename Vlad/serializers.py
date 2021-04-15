from rest_framework import serializers
from .models import VladExelModels
from django.shortcuts import render

class VladExelSerializers(serializers.ModelSerializer):
    file_name = serializers.FileField(max_length=100, allow_empty_file=True, use_url=True, required=False, allow_null=True)
    user_name = serializers.CharField()
    data = serializers.DateField()
    phone_number = serializers.CharField()

    class Meta:
        model = VladExelModels
        fields = ['file_name', 'user_name', 'data', 'phone_number']

    def create(self, validated_data):
        account = VladExelModels(
            file_name=self.validated_data['file_name'],
            user_name=self.validated_data['user_name'],
            data=self.validated_data['data'],
            phone_number=self.validated_data['phone_number'],
        )
        account.save()
        return account



