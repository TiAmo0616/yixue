# Generated by Django 5.0.3 on 2024-04-16 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0011_w_s_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='problem',
            name='jh',
            field=models.CharField(default='0', max_length=32),
        ),
    ]