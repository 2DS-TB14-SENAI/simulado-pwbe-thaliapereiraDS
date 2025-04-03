from django.urls import path
from .views import RegistroUsuarioView, LoginUsuarioView

urlpatterns = [
    path('registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('login/', LoginUsuarioView.as_view(), name='login_usuario'),
]