# Generated by Django 4.0.6 on 2022-07-19 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookshop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_best_selling',
            field=models.BooleanField(default=False),
        ),
    ]