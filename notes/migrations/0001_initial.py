# Generated by Django 3.2.5 on 2022-03-17 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
