# Generated by Django 2.0.7 on 2018-08-08 01:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_auto_20180807_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_comments',
            name='movie_info',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.movie_info'),
        ),
    ]
