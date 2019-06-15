# Generated by Django 2.0 on 2019-04-28 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20190428_0324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('investment_on', models.CharField(max_length=25)),
                ('amount', models.CharField(max_length=8)),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.Event')),
            ],
        ),
    ]