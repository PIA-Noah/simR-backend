# Generated by Django 5.0.6 on 2024-07-09 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_alter_exercise_con'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file',
            name='last_update',
            field=models.DateTimeField(auto_now=True, verbose_name='last update'),
        ),
        migrations.AlterField(
            model_name='share',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]