# Generated by Django 4.1.7 on 2023-04-06 10:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('noticeboardapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notice',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
