from django.urls import path
from . import views

# Esta variable es usada internamente por Django y es recomendada para poder usar URLs dinámicas en los templates HTML
app_name = "polls"

urlpatterns = [
  path('', views.index, name='index'),
  # De esta manera se envía un parámetro en la URL
  path('<int:question_id>/', views.detail, name='detail'),
  path('<int:question_id>/results', views.results, name='results'),
  path('<int:question_id>/votes', views.vote, name='vote'),
]