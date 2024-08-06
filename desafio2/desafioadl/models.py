from django.db import models

# Create your models here.
class Tarea(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(default="") 
    eliminada = models.BooleanField(default=False) 
    
    class Meta:
        db_table = "tarea"
    
class Subtarea(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField(default="") 
    eliminada = models.BooleanField(default=False) 
    id_tarea  = models.ForeignKey(Tarea, on_delete=models.CASCADE)

    class Meta:
        db_table = "subtarea"