# Generated by Django 3.2.9 on 2021-12-04 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
        ('events', '0002_auto_20211204_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='organizer.organizer'),
        ),
    ]
