# Generated by Django 5.0.3 on 2024-06-15 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0017_answer'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(default='', max_length=32)),
                ('comid', models.CharField(default='', max_length=32)),
                ('info', models.TextField(default='')),
                ('username', models.CharField(default='', max_length=32)),
                ('t', models.CharField(max_length=64)),
                ('zan', models.IntegerField()),
            ],
        ),
    ]
