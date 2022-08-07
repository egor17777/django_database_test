# Generated by Django 4.0.6 on 2022-08-07 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0014_alter_book_hero'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='author',
            name='publishing',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='book_app.publishingroom'),
        ),
    ]