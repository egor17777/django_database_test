# Generated by Django 4.0.6 on 2022-08-03 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='the_top_seller',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]