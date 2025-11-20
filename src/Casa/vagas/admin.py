from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Importe os modelos do ficheiro models.py da app 'vagas'
from .models import (
    Usuario, Disciplina, Professor, Aluno, 
    Monitor, Presenca, Mensagem, Relatorio
)

# 1. Personalização para o Modelo Usuario
@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):
    """
    Personaliza o admin para o Usuario customizado.
    Adiciona o campo 'tipo' ao list_display, list_filter e aos fieldsets.
    """
    # Adiciona 'tipo' aos campos exibidos na lista de usuários
    list_display = ('username', 'email', 'first_name', 'last_name', 'tipo', 'is_staff')
    
    # Adiciona 'tipo' como opção de filtro
    list_filter = ('tipo', 'is_staff', 'is_superuser', 'is_active', 'groups')
    
    # Adiciona 'tipo' aos campos de busca
    search_fields = ('username', 'first_name', 'last_name', 'email', 'tipo')
    
    # Adiciona o campo 'tipo' ao fieldset de "Informações Pessoais"
    # Copiamos os fieldsets originais do UserAdmin e modificamos
    fieldsets = list(UserAdmin.fieldsets)
    fieldsets[1] = ('Personal info', {
        'fields': ('first_name', 'last_name', 'email', 'tipo')
    })

# 2. Personalização para o Modelo Disciplina
@admin.register(Disciplina)
class DisciplinaAdmin(admin.ModelAdmin):
    """Personaliza o admin para Disciplina."""
    list_display = ('nome', 'codigo')
    search_fields = ('nome', 'codigo')

# 3. Personalização para o Modelo Professor
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    """
    Personaliza o admin para Professor.
    Usa 'filter_horizontal' para um widget melhor de ManyToMany.
    """
    list_display = ('usuario',)
    search_fields = ('usuario__username', 'usuario__email')
    filter_horizontal = ('disciplina',)  # Melhora a seleção de disciplinas

# 4. Personalização para o Modelo Aluno
@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    """Personaliza o admin para Aluno."""
    list_display = ('usuario', 'matricula')
    search_fields = ('usuario__username', 'usuario__email', 'matricula')

# 5. Personalização para o Modelo Monitor
@admin.register(Monitor)
class MonitorAdmin(admin.ModelAdmin):
    """
    Personaliza o admin para Monitor.
    Usa 'filter_horizontal' para disciplinas.
    """
    list_display = ('usuario', 'horario_fixo')
    search_fields = ('usuario__username', 'usuario__email')
    list_filter = ('disciplinas',)
    filter_horizontal = ('disciplinas',) # Melhora a seleção de disciplinas

# 6. Personalização para o Modelo Presenca
@admin.register(Presenca)
class PresencaAdmin(admin.ModelAdmin):
    """
    Personaliza o admin para Presenca.
    Permite editar o campo 'presente' diretamente da lista.
    """
    list_display = ('aluno', 'monitor', 'disciplina', 'data', 'presente')
    list_filter = ('presente', 'data', 'disciplina', 'monitor')
    search_fields = ('aluno__usuario__username', 'monitor__usuario__username', 'disciplina__nome')
    list_editable = ('presente',) # Permite marcar presença na própria lista
    date_hierarchy = 'data' # Adiciona navegação por data

# 7. Personalização para o Modelo Mensagem
@admin.register(Mensagem)
class MensagemAdmin(admin.ModelAdmin):
    """
    Personaliza o admin para Mensagem.
    Define campos como 'read-only' pois são automáticos.
    """
    list_display = ('remetente', 'destinatario', 'data_envio')
    list_filter = ('data_envio',)
    search_fields = ('remetente__username', 'destinatario__username', 'conteudo')
    readonly_fields = ('data_envio',) # Impede edição da data de envio

# 8. Personalização para o Modelo Relatorio
@admin.register(Relatorio)
class RelatorioAdmin(admin.ModelAdmin):
    """Personaliza o admin para Relatorio."""
    list_display = ('monitor', 'disciplina', 'data')
    list_filter = ('data', 'disciplina', 'monitor')
    search_fields = ('monitor__usuario__username', 'disciplina__nome', 'conteudo')
    readonly_fields = ('data',) # Impede edição da data
    date_hierarchy = 'data'