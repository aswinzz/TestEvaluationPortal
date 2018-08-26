# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Course(models.Model):
    name=models.CharField(max_length=100,default="",blank=True,null=True)
    semester = models.IntegerField(default=1,null=True,blank=True)

    def __str__(self):
        return "{} - {}".format(self.name, self.semester)

    def __unicode__(self):
        return "{} - {}".format(self.namee, self.semester)

    def save(self, *args, **kwargs):
        self.semester = self.name[len(self.name)-4]
        return super(Course, self).save(*args, **kwargs)

class Marks(models.Model):
    user=models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)
    course = models.ForeignKey(Course,null=True,blank=True,on_delete=models.CASCADE)
    marks = models.IntegerField(default=0,null=True,blank=True)
    semester = models.IntegerField(default=1,null=True,blank=True)

    def save(self, *args, **kwargs):
        self.semester = self.course.name[len(self.course.name)-4]
        return super(Marks, self).save(*args, **kwargs)

    def __str__(self):
        return "{} - {} - {}".format(self.user.username, self.course,self.marks)

    def __unicode__(self):
        return "{} - {} - {}".format(self.user.username, self.course,self.marks)
