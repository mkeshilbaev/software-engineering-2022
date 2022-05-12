# Generated by Django 3.1.5 on 2021-03-19 10:20

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnswerOption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_correct', models.BooleanField(default=False)),
                ('image_url', models.ImageField(blank=True, upload_to='answer_option/images')),
                ('image_thumbnail_url', models.ImageField(blank=True, upload_to='answer_option/images')),
                ('text', models.CharField(blank=True, max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='card/images')),
                ('image_thumbnail_url', models.ImageField(blank=True, null=True, upload_to='card/thumbnail/images')),
                ('category', models.CharField(blank=True, max_length=255, null=True)),
                ('time_to_finish', models.PositiveIntegerField(default=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('reward_amount', models.IntegerField(blank=True, default=0, null=True)),
                ('status', models.PositiveIntegerField(choices=[(1, 'Черновик'), (2, 'Утвержден')], default=1)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='course/images')),
                ('image_thumbnail_url', models.ImageField(upload_to='course/thumbnail/images')),
                ('certificate_expiration_day', models.IntegerField(blank=True, null=True)),
                ('certificate_image_url', models.ImageField(blank=True, null=True, upload_to='course/certificate/images')),
                ('certificate_image_thumbnail_url', models.ImageField(blank=True, null=True, upload_to='course/certificate/thumbnail/images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=124)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(blank=True, max_length=400, null=True)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('type', models.PositiveSmallIntegerField(choices=[(1, 'RADIO QUESTION'), (2, 'RADIO IMAGE QUESTION'), (3, 'MULTIPLE QUESTION'), (4, 'OPEN QUESTION'), (5, 'CLOUD QUESTION'), (6, 'PHOTO MARK QUESTION')], default=1)),
                ('is_shuffled', models.BooleanField(default=False)),
                ('time_limit', models.PositiveIntegerField(default=30)),
                ('answer_text', models.CharField(blank=True, max_length=255, null=True)),
                ('answer_order', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None)),
                ('mark_point', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(blank=True, null=True), size=None), size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('answer_option', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_answer_option', to='core.answeroption')),
                ('card', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='question_card', to='core.card')),
            ],
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(blank=True, max_length=1024, null=True)),
                ('order_index', models.PositiveIntegerField(blank=True, null=True)),
                ('image_url', models.ImageField(blank=True, null=True, upload_to='module/images')),
                ('image_thumbnail_url', models.ImageField(blank=True, null=True, upload_to='module/thumbnail/images')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(blank=True, null=True)),
                ('course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='module_course', to='core.course')),
            ],
        ),
        migrations.CreateModel(
            name='FavoriteCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.PositiveIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='favoritecourse_course', to='core.course')),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, related_name='course_tags', to='core.Tag'),
        ),
        migrations.AddField(
            model_name='card',
            name='module',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card_module', to='core.module'),
        ),
    ]
