# Generated by Django 3.2.12 on 2025-01-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('therapist', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='dailyinput',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='dailyinput',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]