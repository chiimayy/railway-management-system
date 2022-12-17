from contextlib import nullcontext
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Register(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.CharField(max_length=10,null=True)
    add = models.CharField(max_length=100,null=True)
    dob = models.DateField(null=True)
    gender = models.CharField(max_length=10,null=True)
    def __str__(self):
        return self.user.first_name



class Add_Train(models.Model):
    id=models.IntegerField(primary_key=True)
    trainname = models.CharField(max_length=30,null=True)
    train_no = models.IntegerField(null=True)
    from_city = models.CharField(max_length=30,null=True)
    to_city = models.CharField(max_length=30,null=True)
    departuretime=models.CharField(max_length=30,null=True)
    arrivaltime=models.CharField(max_length=30,null=True)
    trevaltime=models.CharField(max_length=100,null=True)
    distance=models.IntegerField(null=True)
    secondsitting=models.IntegerField(null=True)
    sleeper=models.IntegerField(null=True)
    threetier=models.IntegerField(null=True)
    twotier=models.IntegerField(null=True)
    chaircar=models.IntegerField(null=True)
    firstclass=models.IntegerField(null=True)
    #img=models.BinaryField()
    def __str__(self):
        return self.trainname+" "+str(self.train_no)

class Add_route(models.Model):
    train = models.ForeignKey(Add_Train,on_delete=models.CASCADE,null=True)
    route = models.CharField(max_length=100,null=True)
    distance=models.IntegerField(null=True)
    fare1=models.IntegerField(null=True)
    fare2=models.IntegerField(null=True)
    fare3=models.IntegerField(null=True)
    fare4=models.IntegerField(null=True)
    fare5=models.IntegerField(null=True)
    fare6=models.IntegerField(null=True)
    def __str__(self):
        return self.route+" "+str(self.train.train_no)

class Passenger(models.Model):
    user = models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    train = models.ForeignKey(Add_Train,on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=30,null=True)
    route=models.CharField(max_length=100,null=True)
    status = models.CharField(max_length=30,null=True)
    date1 = models.DateField(null=True)
    fare = models.IntegerField(null=True)

    def __str__(self):
        return self.user.user.username+" "+self.name

class Book_ticket(models.Model):
    passenger=models.ForeignKey(Passenger,on_delete=models.CASCADE,null=True)
    user=models.ForeignKey(Register,on_delete=models.CASCADE,null=True)
    route=models.CharField(max_length=100,null=True)
    date2=models.DateField(null=True)
    fare=models.IntegerField(null=True)
    def __str__(self):
        return self.user.user.username+" "+self.route

class Asehi(models.Model):
    fare = models.IntegerField(null=True)
    train_name = models.CharField(max_length=30,null=True)
    date3 = models.DateField(null=True)

class contact(models.Model):
    id=models.AutoField(auto_created=True,primary_key=True)
    uname=models.TextField(null=True)
    mailid=models.EmailField(null=True)
    message=models.TextField(null=True)
