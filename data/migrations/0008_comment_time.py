# Generated by Django 5.0.6 on 2024-07-03 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_remove_orgconright_role_remove_userconright_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]