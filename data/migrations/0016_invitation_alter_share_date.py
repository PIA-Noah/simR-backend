# Generated by Django 5.0.6 on 2024-07-12 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_alter_file_last_update_alter_share_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('activated_at', models.DateTimeField(auto_now_add=True)),
                ('expired_at', models.DateTimeField()),
                ('token', models.CharField(max_length=64, unique=True)),
                ('is_used', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ['activated_at'],
            },
        ),
        migrations.AlterField(
            model_name='share',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
