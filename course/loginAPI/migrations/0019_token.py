# Generated by Django 3.2 on 2021-08-25 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginAPI', '0018_users_user_valid_key'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(default='', max_length=40)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loginAPI.users')),
            ],
        ),
    ]
