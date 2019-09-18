# Generated by Django 2.2.5 on 2019-09-18 20:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20190917_2020'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('spotify_id', models.CharField(max_length=1000)),
                ('image_url', models.CharField(max_length=1000)),
                ('artist_name', models.CharField(max_length=200)),
                ('total_tracks', models.IntegerField()),
                ('release_date', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('spotify_id', models.CharField(max_length=1000)),
                ('followers', models.IntegerField()),
                ('image_url', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Profile')),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('spotify_id', models.CharField(max_length=1000)),
                ('preview_url', models.CharField(max_length=1000)),
                ('artist_name', models.CharField(max_length=200)),
                ('duration_ms', models.IntegerField()),
                ('track_number', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Song',
        ),
        migrations.AddField(
            model_name='playlist',
            name='track',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.Track'),
        ),
    ]