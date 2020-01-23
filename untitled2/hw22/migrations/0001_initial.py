# Generated by Django 3.0.2 on 2020-01-21 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_album', models.CharField(default=None, max_length=255)),
                ('year_of_issue', models.CharField(default=None, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.FloatField(default=None, max_length=255)),
                ('duration', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='track', to='hw22.Album')),
            ],
        ),
        migrations.CreateModel(
            name='MusicBand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_band', models.CharField(default=None, max_length=255)),
                ('year_of_foundation', models.CharField(default=None, max_length=255)),
                ('musical_style', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bands', to='hw22.Album')),
            ],
        ),
        migrations.AddField(
            model_name='album',
            name='group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tracks', to='hw22.Track'),
        ),
    ]
