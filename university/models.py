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


# add a 'takes' table to represent the many-to-many relationship between students and courses
class Takes(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField()
    semester = models.CharField(max_length=255)
    year = models.IntegerField()


# add a 'teachers' table to represent teachers
class Teacher(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    teacher_id = models.IntegerField()

    def __str__(self):
        return self.name + " " + self.last_name
