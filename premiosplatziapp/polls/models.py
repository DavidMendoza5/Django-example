from django.db import models
from django.utils import timezone

import datetime

# Django crea el ID automáticamente,lo crea como int autoimcrementable
class Question(models.Model):
  # CharField recibe un parámetro obligatorio que es max_length
  question_text = models.CharField(max_length=200)
  pub_date = models.DateTimeField('date published')

  # Método que sirve para mostrar un campo en específico en la consola interactiva de Django
  def __str__(self):
    return self.question_text
  
  # Método que revisa si una publicación tiene más de un día desde que fue creada
  def was_published_recently(self):
    return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
  # Creación de llave foránea con la opción cascada habilitada
  question = models.ForeignKey(Question, on_delete=models.CASCADE)
  choice_text = models.CharField(max_length=200)
  votes = models.IntegerField(default=0)

  def __str__(self):
    return self.choice_text
