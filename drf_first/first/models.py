from django.db import models

# Create your models here.
class User(models.Model):
    gender_choices = (
        (0, 'male'),
        (1, 'famale'),
        (2, 'other'),
    )
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)

    class Meta:
        db_table = 'user_brf'


class Teacher(models.Model):
    gender_choices = {
        (0, 'male'),
        (1, 'famale'),
        (2, 'other')
    }
    name = models.CharField(max_length=20)
    gender = models.SmallIntegerField(choices=gender_choices, default=0)
    department = models.CharField(max_length=20)
    age = models.IntegerField(null=True)

    class Meta:
        db_table = 'teacher_brf'
        verbose_name = '教师'
        verbose_name_plural = verbose_name
