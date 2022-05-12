# Generated by Django 3.1.5 on 2021-03-20 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(editable=False, help_text='Name of the service.', max_length=100, unique=True)),
                ('host', models.URLField(editable=False, help_text='Host of the service. Ex. auth.example.com', unique=True)),
                ('url', models.URLField(help_text='URL of the proxy to the serviceess')),
            ],
            options={
                'ordering': ['name', 'host'],
            },
        ),
    ]
