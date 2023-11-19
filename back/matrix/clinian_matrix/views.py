from rest_framework import viewsets, permissions
from . permissions import IsOwnerOrReadOnly
from .serializers import *
from .models import *
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .process_data import *
# Create your views here.
class NurseViewSet(viewsets.ModelViewSet):
    queryset = NurseProfile.objects.all()
    serializer_class = NurseProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly] 

class ManagerViewSet(viewsets.ModelViewSet):
    queryset = ManagerProfile.objects.all()
    serializer_class = ManagerProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly] 

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skills.objects.all()
    serializer_class = SkillsSerializer

class PatientsViewSet(viewsets.ModelViewSet):
    queryset = Patients.objects.all()
    serializer_class = PatientSerializer

class CertificateViewSet(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class NurseAssignmentView(APIView):
    patients = Patients.objects.all()
    nurses = NurseProfile.objects.all()
    skills = Skills.objects.all()
    patients_serializer = PatientSerializer(patients, many=True).data
    nurses_serializer = NurseProfileSerializer(nurses, many=True).data
    skill_serializer = SkillsSerializer(skills, many=True).data
    def get(self, request):
        skills, patients, nurses = process(self.patients_serializer, self.nurses_serializer, self.skills)
        return Response({'message': "hi"})
