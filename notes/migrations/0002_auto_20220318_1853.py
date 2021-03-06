# Generated by Django 3.2.5 on 2022-03-18 18:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HashTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(default='exists', max_length=20),
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('text', models.TextField(blank=True, null=True)),
                ('dop', models.DateTimeField(blank=True, null=True)),
                ('dos', models.DateTimeField(blank=True, null=True)),
                ('privacy', models.CharField(default='private', max_length=20)),
                ('hashtags', models.ManyToManyField(blank=True, null=True, to='notes.HashTag')),
                ('tags', models.ManyToManyField(blank=True, null=True, to='notes.Tag')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.user')),
            ],
        ),
    ]
