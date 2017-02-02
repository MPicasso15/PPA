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