# Generated by Django 3.2.12 on 2025-01-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0002_auto_20250115_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='first_name',
            field=models.CharField(default='First_Name', max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='last_name',
            field=models.CharField(default='Last_Name', max_length=30),
        ),
    ]
