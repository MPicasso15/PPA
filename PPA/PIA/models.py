from django.db import models

# Create your models here.

class Indicator(models.Model):
	description = models.TextField()
	expected = models.IntegerField()
	initial_date = models.DateField()
	end_date = models.DateField()
	periodicity = models.IntegerField()
	project = models.ForeignKey(Project, on_delete = models.CASCADE)
	responsible = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return "Proyecto: " + self.project + " ,Responsable: " 
		+ self.responsible + " ,Descripción: " + self.description


class Action(models.Model):
	description = models.TextField()
	number = models.IntegerField()
	project = models.ForeignKey(Project, on_delete = models.CASCADE)

	def __str__(self):
		return "Descripcion: " + self.description


class User(models.Model):
	username = models.CharField(max_length=50)
	password = models.CharField(max_length=50)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Project(models.Model):
	name = models.CharField(max_length=150)
	number = models.IntegerField()

	def __str__(self):
		return self.name


class Review(models.Model):
	reached = models.IntegerField()
	date = models.DateField()
	indicator = models.ForeignKey(Indicator, on_delete=models.CASCADE)

	def __str__(self):
		return self.reached

