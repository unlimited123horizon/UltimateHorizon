# Generated by Django 3.2.7 on 2021-10-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_controlapp', '0004_delete_subjects'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=35)),
                ('date', models.DateField(max_length=30)),
            ],
        ),
    ]
