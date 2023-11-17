from django.db import models
from django.contrib.auth.models import User
import uuid

class NurseProfile(models.Model):
    # options for gender
    options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    user = models.OneToOneField(User, related_name='nurse_profile', on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=20,
        choices=options,
        null=False,
        default='Others',
        blank=False
    )

    def __str__(self) -> str:
        return self.user.username

class ManagerProfile(models.Model):
    # options for gender
    options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    user = models.OneToOneField(User, related_name='manager_profile', on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=20,
        choices=options,
        null=False,
        default='Others',
        blank=False
    )

    def __str__(self) -> str:
        return self.user.username

class Skills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self) -> str:
        return self.name 
    
class Patients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self) -> str:
        return self.name
    
class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self) -> str:
        return self.name
    
class MatchSkills(models.Model):
    nurse = models.OneToOneField(NurseProfile, on_delete=models.CASCADE, primary_key=True)
    level1 = models.ManyToManyField(Skills, related_name='level1_skills', blank=True)
    level2 = models.ManyToManyField(Skills, related_name='level2_skills', blank=True)
    level3 = models.ManyToManyField(Skills, related_name='level3_skills', blank=True)
    certificate = models.ManyToManyField(Certificate, related_name='certificates', blank=True)
    def __str__(self) -> str:
        return self.nurse.user.username