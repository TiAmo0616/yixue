# Generated by Django 5.0.3 on 2024-04-06 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_question_q_ans'),
    ]

    operations = [
        migrations.AlterField(
            model_name='w_s',
            name='t',
            field=models.DateTimeField(default=None),
        ),
    ]
