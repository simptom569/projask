# Generated by Django 3.1.2 on 2020-10-21 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_task',
            field=models.ManyToManyField(default=None, to='task.Task'),
        ),
    ]
