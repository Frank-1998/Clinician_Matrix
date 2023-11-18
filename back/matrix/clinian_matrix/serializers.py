from . models import *
from rest_framework import serializers
from django.contrib.auth.models import User

class NurseProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = NurseProfile
        fields = '__all__'

class ManagerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerProfile
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = '__all__'

class CertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = '__all__'

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'is_nurse'] 
    def create(self, validated_data):
        user = CustomUser(
            email = validated_data['email'],
            username = validated_data['username'],
            is_nurse = validated_data['is_nurse']

        )
        user.set_password(validated_data['password'])
        user.save()
        return user

