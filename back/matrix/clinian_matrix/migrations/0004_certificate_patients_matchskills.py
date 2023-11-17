# Generated by Django 4.2.7 on 2023-11-17 07:05

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('clinian_matrix', '0003_skills_managerprofile_gender_nurseprofile_gender'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='MatchSkills',
            fields=[
                ('nurse', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='clinian_matrix.nurseprofile')),
                ('certificate', models.ManyToManyField(blank=True, null=True, related_name='certificates', to='clinian_matrix.certificate')),
                ('level1', models.ManyToManyField(blank=True, null=True, related_name='level1_skills', to='clinian_matrix.skills')),
                ('level2', models.ManyToManyField(blank=True, null=True, related_name='level2_skills', to='clinian_matrix.skills')),
                ('level3', models.ManyToManyField(blank=True, null=True, related_name='level3_skills', to='clinian_matrix.skills')),
            ],
        ),
    ]
