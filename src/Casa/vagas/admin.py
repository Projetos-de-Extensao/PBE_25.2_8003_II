from django.contrib import admin
from vagas.models import Usuario, Professor, Aluno, Monitor, Disciplina, Presenca, Mensagem, Relatorio

admin.site.register(Usuario)
admin.site.register(Professor)
admin.site.register(Aluno)
admin.site.register(Monitor)
admin.site.register(Disciplina)
admin.site.register(Presenca)
admin.site.register(Mensagem)
admin.site.register(Relatorio)