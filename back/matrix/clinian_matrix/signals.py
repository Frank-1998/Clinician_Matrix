# signals.py
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, NurseProfile, ManagerProfile
@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_nurse:
            NurseProfile.objects.create(user=instance, name=instance.username)
        else:
            ManagerProfile.objects.create(user=instance, name=instance.username)

