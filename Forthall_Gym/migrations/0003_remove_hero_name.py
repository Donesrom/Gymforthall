# Generated by Django 4.1 on 2022-08-20 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Forthall_Gym', '0002_hero_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hero',
            name='name',
        ),
    ]
