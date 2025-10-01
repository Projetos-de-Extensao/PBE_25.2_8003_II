---
id: diagrama_de_casos_de_uso
title: Diagrama de Casos de uso
---

## Casos de Uso

```plantuml
@startuml
skinparam actorStyle awesome
skinparam shadowing false
skinparam rectangle {
  BackgroundColor #F9F9F9
  BorderColor #333
  RoundCorner 15
}
skinparam usecase {
  BackgroundColor #DDEEFF
  BorderColor #333
  ArrowColor #333
  FontSize 14
}

left to right direction

actor "Aluno" as Aluno
actor "Monitor" as Monitor
actor "Coordenação" as Coordenacao

rectangle "App de Monitoria" {
  
  (Buscar monitores) as UC1
  (Agendar sessão) as UC2
  (Cancelar sessão) as UC3
  (Avaliar monitoria) as UC4
  (Candidatar-se a vaga de monitor) as UC5

  (Gerenciar agenda) as UC6
  (Aceitar/recusar solicitações) as UC7
  (Registrar horas) as UC8
  (Consultar histórico) as UC9

  (Aprovar candidatos) as UC10
  (Supervisionar monitores) as UC11
  (Acessar relatórios) as UC12
}

Aluno --> UC1
Aluno --> UC2
Aluno --> UC3
Aluno --> UC4
Aluno --> UC5

Monitor --> UC6
Monitor --> UC7
Monitor --> UC8
Monitor --> UC9

Coordenacao --> UC10
Coordenacao --> UC11
Coordenacao --> UC12
@enduml
