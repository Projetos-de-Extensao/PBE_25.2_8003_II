---
id: diagrama_de_classes 
title: Diagrama de Classes
---

## Diagrama de Classes

```plantuml
@startuml
skinparam classAttributeIconSize 0
skinparam shadowing false
skinparam classBackgroundColor LightBlue
skinparam classBorderColor Black
skinparam classFontSize 14

class Usuario {
  - id
  - nome
  - email
  - senha
  + login()
  + logout()
  + editarPerfil()
  + visualizarPerfil()
}

class Aluno {
  - matricula
  - curso
  + buscarMonitor()
  + agendarSessao()
  + cancelarSessao()
  + avaliarSessao()
  + candidatarMonitor()
}

class Monitor {
  - areaEspecialidade
  - disponibilidade
  + gerenciarAgenda()
  + aceitarSolicitacao()
  + recusarSolicitacao()
  + registrarHoras()
  + consultarHistorico()
}

class Coordenacao {
  - cargo
  - departamento
  + aprovarCandidato()
  + gerarRelatorio()
  + supervisionarMonitores()
}

class Sessao {
  - idSessao
  - data
  - hora
  - status
  - topico
  + confirmar()
  + cancelar()
}

class Candidatura {
  - idCandidatura
  - data
  - status
  + submeter()
  + avaliar()
}

class Relatorio {
  - idRelatorio
  - periodo
  - metricas
  + gerar()
  + exportar()
}

Usuario <|-- Aluno
Usuario <|-- Monitor
Usuario <|-- Coordenacao

Aluno --> Sessao : solicita
Monitor --> Sessao : conduz
Aluno --> Candidatura : envia
Coordenacao --> Candidatura : avalia
Coordenacao --> Relatorio : gera
@enduml
