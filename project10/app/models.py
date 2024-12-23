from django.db import models

# Create your models here.
# class  Grade(models.Model):
#     gradeID=models.IntegerField(unique=True,primary_key=True)
#     loSal=models.IntegerField(null=True)
#     hiSal=models.IntegerField(null=True)

# class GradeDetails(models.Model):
#     detailID=models.IntegerField(unique=True)
#     gradeID=models.ForeignKey(Grade,on_delete=models.CASCADE)
#     Description=models.CharField(max_length=50,unique=True)


class Topic(models.Model):
    Topic_name=models.CharField(unique=True,primary_key=True,max_length=20)
    def __str__(self):
        return self.Topic_name

class Author(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE,null=True)
    email=models.EmailField(default='jhonnysince2000@gmail.com')

class Acess_record(models.Model):
    name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    url=models.URLField()


