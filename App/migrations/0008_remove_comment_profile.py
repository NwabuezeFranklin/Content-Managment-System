# Generated by Django 4.1.7 on 2023-04-04 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0007_comment_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='profile',
        ),
    ]
