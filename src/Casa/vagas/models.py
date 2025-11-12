
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Aluno(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    
    matricula = models.CharField(max_length=50, unique=True, verbose_name="Matrícula")
    curso = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Monitor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    
    area_especialidade = models.CharField(max_length=100, verbose_name="Área de Especialidade")
    disponibilidade = models.TextField(blank=True, help_text="Ex: Segundas 10h-12h, Terças 14h-16h")

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Coordenacao(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Sessao(models.Model):
    STATUS_CHOICES = [
        ('AGENDADA', 'Agendada'),
        ('CONFIRMADA', 'Confirmada'),
        ('CANCELADA', 'Cancelada'),
        ('REALIZADA', 'Realizada'),
    ]

    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='sessoes_solicitadas')
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE, related_name='sessoes_conduzidas')

    data = models.DateField()
    hora = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='AGENDADA')
    topico = models.CharField(max_length=200, verbose_name="Tópico")

    def __str__(self):
        return f"Sessão de {self.topico} em {self.data}"

    def confirmar(self):
        if self.status == 'AGENDADA':
            self.status = 'CONFIRMADA'
            self.save()

    def cancelar(self):
        self.status = 'CANCELADA'
        self.save()


class Candidatura(models.Model):
    STATUS_CHOICES = [
        ('PENDENTE', 'Pendente'),
        ('APROVADA', 'Aprovada'),
        ('REPROVADA', 'Reprovada'),
    ]
    
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='candidaturas')
    avaliador = models.ForeignKey(Coordenacao, on_delete=models.SET_NULL, null=True, blank=True, related_name='candidaturas_avaliadas')

    data_submissao = models.DateField(auto_now_add=True, verbose_name="Data de Submissão")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDENTE')

    def __str__(self):
        return f"Candidatura de {self.aluno} ({self.status})"
        
    def avaliar(self, status, avaliador_user):
        self.status = status
        self.avaliador = avaliador_user
        self.save()


class Relatorio(models.Model):
    gerado_por = models.ForeignKey(Coordenacao, on_delete=models.SET_NULL, null=True, related_name='relatorios_gerados')

    periodo_inicio = models.DateField(verbose_name="Início do Período")
    periodo_fim = models.DateField(verbose_name="Fim do Período")
    data_geracao = models.DateTimeField(auto_now_add=True, verbose_name="Data de Geração")
    
    metricas = models.JSONField(blank=True, null=True, help_text="Dados do relatório em formato JSON")

    def __str__(self):
        return f"Relatório de {self.periodo_inicio} a {self.periodo_fim}"
