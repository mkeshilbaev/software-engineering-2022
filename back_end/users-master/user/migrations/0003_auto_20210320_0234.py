# Generated by Django 3.1.5 on 2021-03-20 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210320_0230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='format 7476486316', max_length=100),
        ),
    ]
