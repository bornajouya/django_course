# Generated by Django 3.2 on 2021-06-13 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginAPI', '0006_auto_20210605_1307'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_one',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.DO_NOTHING, related_name='one', to='loginAPI.users'),
        ),
    ]
