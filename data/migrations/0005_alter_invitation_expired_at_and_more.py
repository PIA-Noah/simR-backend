# Generated by Django 5.0.6 on 2024-07-26 09:33

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_alter_invitation_expired_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitation',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 27, 9, 33, 27, 478447, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='notification',
            name='object',
            field=models.CharField(choices=[('E', 'Exercise'), ('U', 'User'), ('F', 'File'), ('M', 'Comment'), ('C', 'Contract'), ('T', 'Team'), ('R', 'Right')]),
        ),
        migrations.RemoveField(
            model_name='notification',
            name='receiver',
        ),
        migrations.AddField(
            model_name='notification',
            name='receiver',
            field=models.ManyToManyField(db_index=True, null=True, related_name='notification', to=settings.AUTH_USER_MODEL),
        ),
    ]
