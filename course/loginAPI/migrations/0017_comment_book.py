# Generated by Django 3.2 on 2021-08-01 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loginAPI', '0016_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='book',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='loginAPI.book'),
        ),
    ]
