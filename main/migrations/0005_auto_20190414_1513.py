# Generated by Django 2.2 on 2019-04-14 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20190412_2232'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_data',
            old_name='input',
            new_name='data',
        ),
    ]