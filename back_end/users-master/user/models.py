from django.db import models

# User Type
ADMIN = 1
TEACHER = 2
STUDENT = 3

USER_TYPE = (
    (ADMIN, 'ADMIN'),
    (TEACHER, 'TEACHER'),
    (STUDENT, 'STUDENT')
)
# User Gender Type
MALE = 1
FEMALE = 2
DIFFERENT = 3

GENDER_TYPE = (
    (MALE, 'Мужчина'),
    (FEMALE, "Женщина"),
    (DIFFERENT, "Неопрделено")
)


class User(models.Model):
    user_id = models.PositiveIntegerField(unique=True, null=True)
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=155, blank=True)
    phone = models.CharField(max_length=100, blank=True, help_text='format 7476486316')
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE, default=3)
    gender = models.PositiveSmallIntegerField(choices=GENDER_TYPE, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    coins = models.IntegerField(default=0)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f'{self.id}  {self.first_name}  {self.last_name}'

    def is_admin(self):
        if self.user_type == 1:
            return True
        return False

    def is_teacher(self):
        if self.user_type == 2:
            return True
        return False

    def is_student(self):
        if self.user_type == 3:
            return True
        return False