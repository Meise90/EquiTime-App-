# Generated by Django 4.1.7 on 2023-04-06 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scheduleapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.CharField(default='Guest', max_length=50),
        ),
    ]