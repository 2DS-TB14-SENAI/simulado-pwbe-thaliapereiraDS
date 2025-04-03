from django.urls import path
from .views import listar_livros, api_livros

urlpatterns = [
    path('livros/', listar_livros, name='listar_livros'),  # Rota para o template
    path('api/livros/', api_livros, name='api_livros'),     # Rota para a API
]
