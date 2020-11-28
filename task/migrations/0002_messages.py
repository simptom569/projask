# Generated by Django 3.1 on 2020-11-28 21:33

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('message_id', models.CharField(default=uuid.uuid4, max_length=50, primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.users')),
                ('reply', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.messages')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
    ]