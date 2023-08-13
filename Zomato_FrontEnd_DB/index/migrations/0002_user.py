# Generated by Django 4.2.4 on 2023-08-13 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=6)),
                ('order', models.JSONField()),
                ('wallet', models.IntegerField()),
            ],
        ),
    ]
