from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    is_nurse = models.BooleanField(default=False)
    def __str__(self) -> str:
        return self.username

class Skills(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    class Difficiulties(models.IntegerChoices):
        LEVEL1 = 1
        LEVEL2 = 2
        LEVEL3 = 3
    difficiulty = models.IntegerField(default=1, choices=Difficiulties.choices, blank=False, null=False)
    def __str__(self) -> str:
        return self.name 

class Certificate(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self) -> str:
        return self.name

class Patients(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, null=False, blank=False)
    is_stable = models.BooleanField(default=False, blank=False) # if patient is stable
    skills_needed = models.ManyToManyField(Skills, related_name='skills_needed', blank=True)
    def __str__(self) -> str:
        return self.name
class NurseProfile(models.Model):
    # options for gender
    options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    is_jr = models.BooleanField(default=False, blank=True) # if nurse is Junior
    name = models.CharField(max_length=255, blank=False, null=False, default="name")
    user = models.OneToOneField(CustomUser, related_name='nurse_profile', on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=20,
        choices=options,
        null=False,
        default='Others',
        blank=False
    )

    level1 = models.ManyToManyField(Skills, related_name='level1_skills', blank=True)
    level2 = models.ManyToManyField(Skills, related_name='level2_skills', blank=True)
    levle3 = models.ManyToManyField(Skills, related_name='levle3_skills', blank=True)
    levle4 = models.ManyToManyField(Skills, related_name='levle4_skills', blank=True)
    levle5 = models.ManyToManyField(Skills, related_name='levle5_skills', blank=True)
    certificate = models.ManyToManyField(Certificate, related_name='certificate', blank=True)

    def __str__(self) -> str:
        return self.name

class ManagerProfile(models.Model):
    # options for gender
    options = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others')
    )
    name = models.CharField(max_length=255, blank=False, null=False, default="name")
    user = models.OneToOneField(CustomUser, related_name='manager_profile', on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=20,
        choices=options,
        null=False,
        default='Others',
        blank=False
    )

    def __str__(self) -> str:
        return self.user.username