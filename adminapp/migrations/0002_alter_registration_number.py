# Generated by Django 3.2.7 on 2021-09-15 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='number',
            field=models.IntegerField(),
        ),
    ]
