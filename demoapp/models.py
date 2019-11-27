from django.db import models

# Create your models here.

class currentuser(models.Model):
    register_no = models.IntegerField()
    
class Admin(models.Model):
    aid = models.IntegerField(primary_key=True)
    aname = models.CharField(max_length=20)
    apassword = models.CharField(max_length=20)


class Student(models.Model):
    register_no = models.IntegerField(primary_key=True)
    student_email = models.CharField(max_length=40)
    student_name = models.CharField(max_length=20)
    student_marks = models.IntegerField(default=0)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.student_name

class Question(models.Model):
    question_no = models.IntegerField(primary_key=True)
    question_text = models.CharField(max_length=200)
    answer_choice_one = models.CharField(max_length=50)
    answer_choice_two = models.CharField(max_length=50)
    answer_choice_three = models.CharField(max_length=50)
    answer_choice_four = models.CharField(max_length=50)
    answer = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text


class Marks(models.Model):
    register_no = models.IntegerField()
    student_name = models.CharField(max_length=20)
    marks_value = models.IntegerField()
