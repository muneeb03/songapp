# Generated by Django 4.2.4 on 2023-08-22 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite_songs',
            field=models.ManyToManyField(blank=True, related_name='favorited_by', to='songs.song'),
        ),
    ]
