# Generated by Django 2.0 on 2019-04-27 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_article'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title',
        ),
    ]