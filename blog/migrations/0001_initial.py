# Generated by Django 5.0.1 on 2024-01-10 16:52

import cloudinary.models
import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Lizard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(default='default', max_length=255, verbose_name='image')),
                ('created_on', models.DateField(auto_now_add=True)),
                ('max_size', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('lifespan', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price_from', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('price_to', models.IntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('diet', models.IntegerField(choices=[(0, 'Not defined'), (1, 'Omnivorous'), (2, 'Herbivorous'), (3, 'Insectivorous')], default=0)),
                ('diet_list', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lizard_post', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('created_on', models.DateField(auto_now_add=True)),
                ('is_question', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.lizard')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
