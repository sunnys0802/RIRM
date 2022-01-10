from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    roll_no = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    class_name = models.CharField(max_length=500)
    school = models.CharField(max_length=500)
    mobile = models.BigIntegerField()
    address = models.CharField(max_length=500)

    def __str__(self):
        return self.name



class StudentAcademics(models.Model):
    roll_no = models.ForeignKey(StudentInfo, on_delete=models.CASCADE, null=True, blank=True)
    math = models.IntegerField(default=0)
    physics = models.IntegerField(default=0)
    chemistry = models.IntegerField(default=0)
    biology = models.IntegerField(default=0)
    english = models.IntegerField(default=0)
   
    def __str__(self):
        return (self.roll_no)


