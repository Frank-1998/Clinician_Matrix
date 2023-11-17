# Generated by Django 4.2.7 on 2023-11-17 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinian_matrix', '0004_certificate_patients_matchskills'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matchskills',
            name='level1',
            field=models.ManyToManyField(blank=True, related_name='level1_skills', to='clinian_matrix.skills'),
        ),
        migrations.AlterField(
            model_name='matchskills',
            name='level2',
            field=models.ManyToManyField(blank=True, related_name='level2_skills', to='clinian_matrix.skills'),
        ),
        migrations.AlterField(
            model_name='matchskills',
            name='level3',
            field=models.ManyToManyField(blank=True, related_name='level3_skills', to='clinian_matrix.skills'),
        ),
    ]
