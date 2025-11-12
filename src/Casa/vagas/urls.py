from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

# Cria um router e registra nossos viewsets com ele.
router = DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'disciplinas', views.DisciplinaViewSet)
router.register(r'professores', views.ProfessorViewSet)
router.register(r'alunos', views.AlunoViewSet)
router.register(r'monitores', views.MonitorViewSet)
router.register(r'presencas', views.PresencaViewSet)
router.register(r'mensagens', views.MensagemViewSet)
router.register(r'relatorios', views.RelatorioViewSet)

# As URLs da API são determinadas automaticamente pelo router.
urlpatterns = [
    path('', include(router.urls)),
]
