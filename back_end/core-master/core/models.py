from django.db import models
from django.contrib.postgres.fields import ArrayField


# Course
DRAFT = 1
APPROVED = 2

COURSE_STATUS = (
    (DRAFT, 'Черновик'),
    (APPROVED, 'Утвержден')
)

# Question
RADIO = 1
RADIO_IMAGE = 2
MULTIPLE = 3
OPEN = 4
CLOUD = 5
PHOTO_MARK = 6

QUESTION_TYPE = (
    (RADIO, 'RADIO QUESTION'),
    (RADIO_IMAGE, 'RADIO IMAGE QUESTION'),
    (MULTIPLE, 'MULTIPLE QUESTION'),
    (OPEN, 'OPEN QUESTION'),
    (CLOUD, 'CLOUD QUESTION'),
    (PHOTO_MARK, 'PHOTO MARK QUESTION'),
)


class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    reward_amount = models.IntegerField(blank=True, null=True, default=0)
    status = models.PositiveIntegerField(choices=COURSE_STATUS, default=1)
    image_url = models.ImageField(upload_to='course/images', blank=True, null=True)
    image_thumbnail_url = models.ImageField(upload_to='course/thumbnail/images', blank=True, null=True)
    certificate_expiration_day = models.IntegerField(blank=True, null=True)
    certificate_image_url = models.ImageField(upload_to='course/certificate/images', blank=True, null=True)
    certificate_image_thumbnail_url = models.ImageField(upload_to='course/certificate/thumbnail/images',
                                                        blank=True, null=True)
    tags = models.ManyToManyField(to='Tag', related_name='%(class)s_tags', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)

    def __str__(self):
        return f'{self.id}   {self.name}'


class Tag(models.Model):
    name = models.CharField(max_length=124)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}  {self.name}'


class FavoriteCourse(models.Model):
    user_id = models.PositiveIntegerField(blank=False, null=False)
    course = models.ForeignKey(to='Course', on_delete=models.CASCADE,
                               related_name='%(class)s_course')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}---{self.course.name}----{self.user_id}'


class Module(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    course = models.ForeignKey(to='Course', related_name='%(class)s_course', on_delete=models.SET_NULL, blank=True, null=True)
    order_index = models.PositiveIntegerField(blank=True, null=True)
    image_url = models.ImageField(upload_to='module/images', blank=True, null=True)
    image_thumbnail_url = models.ImageField(upload_to='module/thumbnail/images', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}--{self.name}'


class Card(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1024, blank=True, null=True)
    image_url = models.ImageField(upload_to='card/images', blank=True, null=True)
    image_thumbnail_url = models.ImageField(upload_to='card/thumbnail/images', blank=True, null=True)
    module = models.ForeignKey(to='Module', on_delete=models.SET_NULL, related_name='%(class)s_module', blank=True, null=True)
    category = models.CharField(max_length=255, blank=True, null=True)
    time_to_finish = models.PositiveIntegerField(default=30)  # seconds
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}   {self.name}'


class Question(models.Model):
    card = models.ForeignKey(to='Card', on_delete=models.SET_NULL, related_name='%(class)s_card', blank=True, null=True)
    question_text = models.CharField(max_length=400, blank=True, null=True)
    description = models.CharField(max_length=1024, blank=True, null=True)
    type = models.PositiveSmallIntegerField(choices=QUESTION_TYPE, default=1)
    is_shuffled = models.BooleanField(default=False)
    time_limit = models.PositiveIntegerField(default=30)  # seconds
    answer_option = models.ForeignKey(to='AnswerOption', related_name='%(class)s_answer_option',
                                      blank=True, on_delete=models.SET_NULL, null=True)
    answer_text = models.CharField(max_length=255, blank=True, null=True)
    answer_order = ArrayField(models.IntegerField(blank=True, null=True), null=True, blank=True)
    mark_point = ArrayField(models.FloatField(blank=True, null=True), null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}  {self.question_text}'


class AnswerOption(models.Model):
    is_correct = models.BooleanField(default=False)
    image_url = models.ImageField(upload_to='answer_option/images', blank=True)
    image_thumbnail_url = models.ImageField(upload_to='answer_option/images', blank=True)
    text = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}  {self.text}'

