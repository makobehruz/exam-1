# Generated by Django 5.1.3 on 2024-11-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Taxi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('plate', models.CharField(max_length=50)),
                ('driver', models.CharField(max_length=100, unique=True)),
                ('passenger', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=25)),
                ('statsu', models.CharField(max_length=50)),
            ],
        ),
    ]
