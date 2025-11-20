from rest_framework import serializers
from .models import (
    Usuario, Disciplina, Professor, Aluno, 
    Monitor, Presenca, Mensagem, Relatorio
)

class UsuarioSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Usuario, expondo campos seguros."""
    class Meta:
        model = Usuario
        # Excluímos campos sensíveis como 'password' e 'user_permissions'
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'tipo']

class DisciplinaSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Disciplina."""
    class Meta:
        model = Disciplina
        fields = '__all__'

class ProfessorSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Professor."""
    class Meta:
        model = Professor
        fields = '__all__'

class AlunoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Aluno."""
    class Meta:
        model = Aluno
        fields = '__all__'

class MonitorSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Monitor."""
    class Meta:
        model = Monitor
        fields = '__all__'

class PresencaSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Presenca."""
    class Meta:
        model = Presenca
        fields = '__all__'

class MensagemSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Mensagem."""
    class Meta:
        model = Mensagem
        fields = '__all__'

class RelatorioSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Relatorio."""
    class Meta:
        model = Relatorio
        fields = '__all__'

class VagaMonitoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = VagaMonitoria
        fields = '__all__'
