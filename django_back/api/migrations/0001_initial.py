# Generated by Django 5.0.4 on 2024-04-19 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='django_back',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fan', models.FloatField()),
                ('Refrigerator', models.FloatField()),
                ('Television', models.FloatField()),
                ('MonthlyHours', models.FloatField()),
            ],
        ),
    ]
