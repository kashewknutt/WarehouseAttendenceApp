# Generated by Django 5.0.6 on 2024-06-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_facial_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='facial_data',
        ),
        migrations.AddField(
            model_name='employee',
            name='face_encoding',
            field=models.TextField(blank=True, null=True),
        ),
    ]
