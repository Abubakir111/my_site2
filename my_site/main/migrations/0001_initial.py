# Generated by Django 5.0.1 on 2024-01-19 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя:')),
                ('date', models.DateTimeField(verbose_name='Дата публикаций')),
            ],
        ),
    ]
