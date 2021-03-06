# Generated by Django 2.2 on 2020-03-30 11:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=120)),
                ('category', models.CharField(max_length=120)),
                ('slug', models.SlugField(unique=True)),
                ('title', models.CharField(max_length=120)),
                ('image1', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field')),
                ('image2', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field')),
                ('image3', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field')),
                ('image4', models.ImageField(blank=True, height_field='height_field', null=True, upload_to='images/', width_field='width_field')),
                ('height_field', models.IntegerField(default=0)),
                ('width_field', models.IntegerField(default=0)),
                ('content', models.TextField()),
                ('publish_date', models.DateField()),
                ('update', models.DateTimeField(auto_now=True)),
                ('Timestamp', models.DateTimeField(auto_now=True)),
                ('draft', models.BooleanField(default=False)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
