# Generated by Django 2.2.4 on 2024-05-17 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('film_actor_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='category',
        ),
        migrations.AddField(
            model_name='movie',
            name='categories',
            field=models.ManyToManyField(related_name='Movies', to='film_actor_app.Category'),
        ),
    ]
