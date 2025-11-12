
---

id: diagrama_de_classes

title: Diagrama de Classes

---



## Diagrama de Classes


```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam shadowing false
skinparam classBackgroundColor LightGreen
skinparam classBorderColor Black
skinparam classFontSize 14

' --- Definição das Classes (Models) ---

class Usuario {
.. Atributos ..
+ tipo 
}

class Disciplina {
.. Atributos ..
+ nome
+ codigo
}

class Professor {
' (Perfil do Usuario)
}

class Aluno {
.. Atributos ..
+ matricula
' (Perfil do Usuario)
}

class Monitor {
.. Atributos ..
+ horario_fixo
' (Perfil do Usuario)
}

class Presenca {
.. Atributos ..
+ data
+ presente
}

class Mensagem {
.. Atributos ..
+ conteudo
+ data_envio
}

class Relatorio {
.. Atributos ..
+ data
+ conteudo
}

' --- Relacionamentos de Perfil (OneToOneField) ---
' Um Usuário tem um perfil de Aluno, Monitor OU Professor
Usuario "1" -- "1" Aluno : usuario
Usuario "1" -- "1" Monitor : usuario
Usuario "1" -- "1" Professor : usuario

' --- Relacionamentos de Disciplina (ManyToManyField) ---
' Professores e Monitores podem ter várias Disciplinas
Professor "n" -- "n" Disciplina : disciplina
Monitor "n" -- "n" Disciplina : disciplinas

' --- Relacionamentos da Presenca (ForeignKey) ---
' Presenca é uma classe de associação
Presenca "n" --> "1" Aluno : aluno
Presenca "n" --> "1" Monitor : monitor
Presenca "n" --> "1" Disciplina : disciplina

' --- Relacionamentos do Relatorio (ForeignKey) ---
Relatorio "n" --> "1" Monitor : monitor
Relatorio "n" --> "1" Disciplina : disciplina

' --- Relacionamentos da Mensagem (ForeignKey Reflexivo) ---
' Mensagem aponta para Usuário duas vezes
Mensagem "n" --> "1" Usuario : remetente
Mensagem "n" --> "1" Usuario : destinatario

@enduml
```