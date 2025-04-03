from django.urls import path
from .views import RegistroUsuarioView, LoginUsuarioView

urlpatterns = [
    path('auth/registro/', RegistroUsuarioView.as_view(), name='registro_usuario'),
    path('auth/login/', LoginUsuarioView.as_view(), name='login_usuario'),
]