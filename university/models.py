from django.db import models


# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    student_id = models.IntegerField()
    birth_date = models.DateField()

    def __str__(self):
        return self.name + " " + self.last_name


class Course(models.Model):
    name = models.CharField(max_length=255)
    course_id = models.IntegerField()
    semester = models.CharField(max_length=255)
    credit = models.IntegerField()

