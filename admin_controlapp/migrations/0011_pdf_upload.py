# Generated by Django 3.2.7 on 2021-10-26 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_controlapp', '0010_auto_20211025_2108'),
    ]

    operations = [
        migrations.CreateModel(
            name='PDf_upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cls', models.CharField(max_length=2)),
                ('sub', models.CharField(max_length=20)),
                ('sub_name', models.CharField(max_length=100)),
                ('pdf', models.URLField()),
                ('up_date', models.DateField(max_length=20)),
            ],
        ),
    ]
