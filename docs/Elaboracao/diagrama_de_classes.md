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
  ' Perfil do Usuario
}

class Aluno {
  .. Atributos ..
  + matricula
}

class Monitor {
  .. Atributos ..
  + horario_fixo
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

' --- classe adicionada ---
class Vaga {
  .. Atributos ..
  + numero_vagas
  + prerequisitos
  + responsabilidades
  + status
}

' --- Relacionamentos de Perfil ---
Usuario "1" -- "1" Aluno : usuario
Usuario "1" -- "1" Monitor : usuario
Usuario "1" -- "1" Professor : usuario

' --- Relacionamentos de Disciplina ---
Professor "1" -- "n" Disciplina : ministra
Monitor "n" -- "n" Disciplina : apoia

' --- Relacionamentos da Presenca ---
Presenca "n" --> "1" Aluno : aluno
Presenca "n" --> "1" Monitor : monitor
Presenca "n" --> "1" Disciplina : disciplina

' --- Relacionamentos do Relatorio ---
Relatorio "n" --> "1" Monitor : monitor
Relatorio "n" --> "1" Disciplina : disciplina

' --- Relacionamentos da Mensagem ---
Mensagem "n" --> "1" Usuario : remetente
Mensagem "n" --> "1" Usuario : destinatario

' --- Relacionamentos de Vaga ---
Vaga "n" --> "1" Professor : professor
Vaga "n" --> "1" Disciplina : disciplina

@enduml
