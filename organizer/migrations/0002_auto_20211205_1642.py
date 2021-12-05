# Generated by Django 3.2.9 on 2021-12-05 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organizer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('postal_code', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='organizer',
            name='address',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='organizer.address'),
        ),
    ]
