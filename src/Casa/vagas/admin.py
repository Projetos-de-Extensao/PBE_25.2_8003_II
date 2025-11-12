from django.contrib import admin
from vagas.models import  Aluno, Monitor, Coordenacao, Sessao, Candidatura, Relatorio


admin.site.register(Aluno)
admin.site.register(Monitor)
admin.site.register(Coordenacao)
admin.site.register(Sessao)
admin.site.register(Candidatura)
admin.site.register(Relatorio)