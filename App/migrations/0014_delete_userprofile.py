# Generated by Django 4.1.7 on 2023-04-09 10:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0013_userprofile_delete_userpreference'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
