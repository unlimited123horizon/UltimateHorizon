# Generated by Django 3.2.7 on 2021-09-15 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('username', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=30, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=25)),
                ('number', models.IntegerField(max_length=13)),
                ('gender', models.CharField(max_length=6)),
                ('address', models.CharField(max_length=100)),
                ('city', models.TextField(max_length=20)),
                ('standard', models.CharField(max_length=2)),
            ],
        ),
    ]