# Generated by Django 3.1.5 on 2021-04-02 06:42

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210327_0756'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='mark_point',
        ),
        migrations.AlterField(
            model_name='question',
            name='answer_order',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), blank=True, null=True, size=None),
        ),
    ]