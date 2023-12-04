from django.db import models

# Create your models here.
ID_LEN = 8
NAME_LEN = 20
PASSWD_LEN = 20
COURSENAME_LEN = 40


class Student(models.Model):
    id = models.CharField(max_length=ID_LEN, verbose_name='学号', primary_key=True)
    name = models.CharField(max_length=NAME_LEN)
    password = models.CharField(max_length=PASSWD_LEN)

    class Meta:
        db_table = 'students'
        verbose_name = '学生'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Teacher(models.Model):
    id = models.CharField(max_length=ID_LEN, verbose_name='工号', primary_key=True)
    name = models.CharField(max_length=NAME_LEN)
    password = models.CharField(max_length=PASSWD_LEN)

    class Meta:
        db_table = 'teachers'
        verbose_name = '教师'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.id


class Course(models.Model):
    id = models.CharField(max_length=ID_LEN, verbose_name='课程号', primary_key=True)
    name = models.CharField(max_length=COURSENAME_LEN)
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name='授课教师'),
    time = models.CharField(max_length=30, verbose_name='上课时间')
    location = models.CharField(max_length=30, verbose_name='上课地点')
    year = models.IntegerField(verbose_name='年份', default=2023)
    semester = models.IntegerField(verbose_name='学期', default=1)  # 1:秋季学期，0:春季学习

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.id


class StudentCourse(models.Model):
    s_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    c_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.IntegerField(verbose_name='成绩', null=True)

    class Meta:
        db_table = 'student_course'
        unique_together = (("s_id", "c_id"),)
