from django.db import models

# Django crea el ID automáticamente,lo crea como int autoimcrementable
class Question(models.Model):
  # CharField recibe un parámetro obligatorio que es max_length
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

class Choice(models.Model):
  # Creación de llave foránea con la opción cascada habilitada
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)
