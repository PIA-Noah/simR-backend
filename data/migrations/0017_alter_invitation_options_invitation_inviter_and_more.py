# Generated by Django 5.0.6 on 2024-07-15 08:43

import datetime
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0016_invitation_alter_share_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='invitation',
            options={'ordering': ['-activated_at']},
        ),
        migrations.AddField(
            model_name='invitation',
            name='inviter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='invitation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='expired_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 16, 8, 43, 28, 244958, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='invitation',
            name='token',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=64, unique=True),
        ),
    ]
