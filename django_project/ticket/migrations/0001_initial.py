# Generated by Django 5.1.1 on 2024-09-20 15:50

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_nu', models.UUIDField(default=uuid.uuid4)),
                ('title', models.CharField(max_length=100)),
                ('discription', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('isresolved', models.BooleanField(default=False)),
                ('accepted_date', models.DateTimeField(blank=True, null=True)),
                ('closed_date', models.DateTimeField(blank=True, null=True)),
                ('ticket_stat', models.CharField(max_length=100)),
            ],
        ),
    ]
