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
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def get_queryset(self):
        query_params = self.request.query_params
        if not query_params:
            return self.queryset
        print(query_params['user'])
        return self.queryset.filter(user=query_params['user'])


class ManagerViewSet(viewsets.ModelViewSet):
    queryset = ManagerProfile.objects.all()
    serializer_class = ManagerProfileSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]


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
        skills, patients, jr_nurses, sr_nurses = process(
            self.patients_serializer, self.nurses_serializer, self.skills)
        assignments, unassigned_complex_patients, unassigned_non_complex_patients, nurses_to_be_trained = assign(
            sr_nurses, jr_nurses, patients)
        print(assignments)
        print(unassigned_complex_patients),
        print(unassigned_non_complex_patients),
        print(nurses_to_be_trained)
        return Response({'assignment': assignments, 'unassigned_complex_pt': unassigned_complex_patients, 'unassigned_non_complex_pt': unassigned_non_complex_patients, "nurses_to_be_trained": nurses_to_be_trained})
