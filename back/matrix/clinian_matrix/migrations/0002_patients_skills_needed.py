# Generated by Django 4.2.7 on 2023-11-18 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinian_matrix', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='skills_needed',
            field=models.ManyToManyField(blank=True, related_name='skills_needed', to='clinian_matrix.skills'),
        ),
    ]