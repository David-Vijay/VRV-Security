# Generated by Django 5.1.3 on 2024-11-30 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_crud_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crud',
            name='status',
            field=models.CharField(max_length=50),
        ),
    ]
