# Generated by Django 4.1.1 on 2022-09-12 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flower',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
