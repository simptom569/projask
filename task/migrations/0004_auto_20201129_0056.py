# Generated by Django 3.1 on 2020-11-28 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20201129_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messages',
            name='reply',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='task.messages'),
        ),
    ]