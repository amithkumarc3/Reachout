# Generated by Django 2.0 on 2019-06-09 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_organizers_map'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='assiged_By',
            new_name='assigned_by',
        ),
    ]
