from django.db import models

class reg(models.Model):
    sname=models.CharField(max_length=20,primary_key=True)
    spas=models.CharField(max_length=15)
    semail=models.CharField(max_length=50)
    sphone=models.CharField(max_length=10)
    sloc=models.CharField(max_length=50)

class pho(models.Model):
	photo=models.CharField(max_length=60)
	date1=models.CharField(max_length=60)


class pho1(models.Model):
	photo=models.CharField(max_length=60)
	date1=models.CharField(max_length=60)
	Time1=models.CharField(max_length=60)


class pho2(models.Model):
	photo=models.CharField(max_length=60)
	date1=models.CharField(max_length=60)
	Time1=models.CharField(max_length=60)
	des=models.CharField(max_length=100)

class pho3(models.Model):
	photo=models.CharField(max_length=60)
	date1=models.CharField(max_length=60)
	Time1=models.CharField(max_length=60)
	des=models.CharField(max_length=100)
	Status=models.CharField(max_length=50)

class pho4(models.Model):
	photo=models.CharField(max_length=60)
	date1=models.CharField(max_length=60)
	Time1=models.CharField(max_length=60)
	des=models.CharField(max_length=100)
	Status=models.CharField(max_length=50)
	Location=models.CharField(max_length=150)


class loc(models.Model):
	lat=models.CharField(max_length=100)
	lang=models.CharField(max_length=100)



