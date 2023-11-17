from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(NurseProfile)
admin.site.register(ManagerProfile)
admin.site.register(Skills)
admin.site.register(Patients)
admin.site.register(Certificate)
admin.site.register(MatchSkills)