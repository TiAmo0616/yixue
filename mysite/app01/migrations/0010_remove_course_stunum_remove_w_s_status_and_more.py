# Generated by Django 5.0.3 on 2024-04-11 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0009_question_a_question_b_question_c_question_d'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='stuNum',
        ),
        migrations.RemoveField(
            model_name='w_s',
            name='status',
        ),
        migrations.AddField(
            model_name='question',
            name='score',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AddField(
            model_name='s_q',
            name='judgement',
            field=models.TextField(default='无'),
        ),
        migrations.AddField(
            model_name='s_q',
            name='score',
            field=models.CharField(default='', max_length=32),
        ),
    ]
