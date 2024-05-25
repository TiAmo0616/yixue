# Generated by Django 5.0.3 on 2024-05-25 08:11

import builtins
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0016_learningmaterials'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='id',
            field=models.BigAutoField(auto_created=True, default=builtins.id, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
