# Generated by Django 3.2.9 on 2021-12-05 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_event_organizer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='events.Tag'),
        ),
    ]