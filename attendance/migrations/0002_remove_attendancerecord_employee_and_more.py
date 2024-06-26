# Generated by Django 5.0.6 on 2024-06-12 15:38

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendancerecord',
            name='employee',
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='notes',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('absent', 'Absent')], default='present', max_length=20),
        ),
        migrations.AddField(
            model_name='attendancerecord',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='check_in_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='check_out_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='attendancerecord',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
