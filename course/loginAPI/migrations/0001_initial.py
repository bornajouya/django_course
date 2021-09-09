# Generated by Django 3.2 on 2021-05-29 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(default='', max_length=40)),
                ('user_lastname', models.CharField(default='', max_length=80)),
                ('user_photo', models.ImageField(null=True, upload_to='media')),
                ('user_addres', models.TextField(default='', max_length=400)),
                ('user_phone', models.IntegerField(default=912)),
            ],
        ),
    ]
