# Generated by Django 3.1 on 2020-12-05 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0005_users_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=50),
        ),
    ]