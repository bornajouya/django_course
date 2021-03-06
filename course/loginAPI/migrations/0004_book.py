# Generated by Django 3.2 on 2021-06-02 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginAPI', '0003_alter_users_user_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100)),
                ('author', models.CharField(default='', max_length=200)),
                ('price', models.FloatField(default=0)),
                ('pages', models.IntegerField(default=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='books')),
            ],
        ),
    ]
