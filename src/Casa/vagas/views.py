from rest_framework import viewsets
from .models import (
    Usuario, Disciplina, Professor, Aluno, 
    Monitor, Presenca, Mensagem, Relatorio
)
from .serializers import (
    UsuarioSerializer, DisciplinaSerializer, ProfessorSerializer, AlunoSerializer, 
    MonitorSerializer, PresencaSerializer, MensagemSerializer, RelatorioSerializer
)

class UsuarioViewSet(viewsets.ModelViewSet):
    """Endpoint da API para visualização e edição de Usuários."""
    queryset = Usuario.objects.all().order_by('-date_joined')
    serializer_class = UsuarioSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    """Endpoint da API para visualização e edição de Disciplinas."""
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class ProfessorViewSet(viewsets.ModelViewSet):
    """Endpoint da API para visualização e edição de Professores."""
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    """Endpoint da API para visualização e edição de Alunos."""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class MonitorViewSet(viewsets.ModelViewSet):
    """Endpoint da API para visualização e edição de Monitores."""
    queryset = Monitor.objects.all()
    serializer_class = MonitorSerializer

class PresencaViewSet(viewsets.ModelViewSet):
    """Endpoint da API para visualização e edição de Presenças."""
    queryset = Presenca.objects.all()
    serializer_class = PresencaSerializer

class MensagemViewSet(viewsets.ModelViewSet):
    """Endpoint da API para visualização e edição de Mensagens."""
    queryset = Mensagem.objects.all()
    serializer_class = MensagemSerializer

class RelatorioViewSet(viewsets.ModelViewSet):
    """Endpoint da API para visualização e edição de Relatórios."""
    queryset = Relatorio.objects.all()
    serializer_class = RelatorioSerializer

from rest_framework import viewsets, permissions
from .models import VagaMonitoria
from .serializers import VagaMonitoriaSerializer
from rest_framework.exceptions import PermissionDenied

class VagaMonitoriaViewSet(viewsets.ModelViewSet):
    queryset = VagaMonitoria.objects.all()
    serializer_class = VagaMonitoriaSerializer

    def perform_create(self, serializer):
        professor = serializer.validated_data["professor"]
        disciplina = serializer.validated_data["disciplina"]

        # Regra de negócio: professor só cria vaga da disciplina dele
        if disciplina not in professor.disciplina.all():
            raise PermissionDenied("Este professor não leciona essa disciplina.")

        serializer.save()
