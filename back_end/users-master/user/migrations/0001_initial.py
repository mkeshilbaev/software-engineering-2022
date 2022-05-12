# Generated by Django 3.1.5 on 2021-03-20 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('middle_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=155)),
                ('phone', models.IntegerField(blank=True, max_length=11)),
                ('user_type', models.PositiveSmallIntegerField(choices=[(1, 'ADMIN'), (2, 'TEACHER'), (3, 'STUDENT')], default=3)),
                ('gender', models.PositiveSmallIntegerField(choices=[(1, 'Мужчина'), (2, 'Женщина'), (3, 'Неопрделено')], default=3)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
