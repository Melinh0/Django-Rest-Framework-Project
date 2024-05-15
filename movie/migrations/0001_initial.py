# Generated by Django 5.0.5 on 2024-05-13 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('director', models.CharField(max_length=100, verbose_name='Director')),
                ('duration', models.IntegerField(verbose_name='Duration')),
            ],
        ),
    ]
