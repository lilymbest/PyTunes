# Generated by Django 2.2.5 on 2019-09-16 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_token', models.CharField(max_length=300)),
                ('refresh_token', models.CharField(max_length=300)),
                ('spotify_id', models.CharField(max_length=100)),
                ('spotify_display_name', models.CharField(max_length=100)),
                ('spotify_product', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]