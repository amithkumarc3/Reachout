# Generated by Django 2.0 on 2019-06-10 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_auto_20190609_1857'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='organizers_map',
            name='event_id',
        ),
        migrations.RemoveField(
            model_name='organizers_map',
            name='user_id',
        ),
        migrations.AddField(
            model_name='event',
            name='amount',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Organizers_map',
        ),
    ]