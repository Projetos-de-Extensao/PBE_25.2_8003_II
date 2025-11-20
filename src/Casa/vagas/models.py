from django.db import models
from django.contrib.auth.models import AbstractUser


class Usuario(AbstractUser):
    """
    Modelo de usuário customizado que estende o AbstractUser padrão.
    Adiciona um campo 'tipo' para controle de permissões e papéis.
    """
    TIPO_USUARIO = [
        ('aluno', 'Aluno'),
        ('monitor', 'Monitor'),
        ('professor', 'Professor'),
        ('admin', 'Administrador'),
    ]
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default='aluno')

    def __str__(self):
        return f"{self.username} ({self.get_tipo_display()})"


class Disciplina(models.Model):
    """
    Modelo para representar as disciplinas oferecidas.
    """
    nome = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.nome


class Professor(models.Model):
    """
    Modelo que vincula um Usuário com tipo 'professor' a 
    uma ou mais Disciplinas que ele leciona.
    """
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    disciplina = models.ManyToManyField(Disciplina, related_name='professores')

    def __str__(self):
        return self.usuario.username


class Aluno(models.Model):
    """
    Modelo que vincula um Usuário com tipo 'aluno' e 
    armazena sua matrícula.
    """
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    matricula = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.usuario.username


class Monitor(models.Model):
    """
    Modelo que vincula um Usuário com tipo 'monitor' às 
    disciplinas das quais ele é monitor e seu horário fixo.
    """
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    disciplinas = models.ManyToManyField(Disciplina, related_name='monitores')
    horario_fixo = models.CharField(max_length=100, help_text="Ex: Segunda 10h-12h")

    def __str__(self):
        return self.usuario.username


class Presenca(models.Model):
    """
    Registra a presença de um Aluno em uma monitoria,
    indicando o Monitor, a Disciplina e a data.
    """
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    presente = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.aluno.usuario.username} - {self.disciplina.nome} ({self.data})"


class Mensagem(models.Model):
    """
    Modelo para um sistema simples de troca de mensagens
    entre dois Usuários (remetente e destinatário).
    """
    remetente = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens_enviadas')
    destinatario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='mensagens_recebidas')
    conteudo = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.remetente.username} → {self.destinatario.username}"


class Relatorio(models.Model):
    """
    Permite que um Monitor submeta relatórios de atividades
    para uma disciplina específica.
    """
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    conteudo = models.TextField()

    def __str__(self):
        return f"Relatório de {self.monitor.usuario.username} - {self.disciplina.nome}"
    
class VagaMonitoria(models.Model):
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE, related_name="vagas")
    disciplina = models.ForeignKey(Disciplina, on_delete=models.CASCADE, related_name="vagas")
    numero_vagas = models.IntegerField()
    prerequisitos = models.TextField()
    responsabilidades = models.TextField()
    status = models.CharField(max_length=20, default="aberta")  # aberta / fechada / preenchida

    def __str__(self):
        return f"Vaga de {self.disciplina.nome} ({self.numero_vagas} vagas)"
