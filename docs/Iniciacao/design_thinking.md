---
id: dt
title: Design Thinking
---

## **Design Thinking**

### **1. Capa**

- Título do Projeto : Sistema de Monitoria IBMEC
- Nome da Equipe : Antonio José Vieira, Fabio Henrique Vasconcellos, Rafael Paraquett
- Data : iniciado em 04/08/2025

---

### **2. Introdução**

- **Contexto do Projeto**: O atual sistema de monitoria acadêmica é descentralizado, operando de forma manual através de e-mails, planilhas e aplicativos de mensagens. Essa fragmentação gera ineficiência, dificulta o acesso dos alunos à ajuda, sobrecarrega os monitores com tarefas administrativas e impede a coordenação de gerir o programa de forma estratégica por falta de dados centralizados.
- **Objetivo**: Potencializar o sucesso acadêmico dos alunos e aprimorar a qualidade do ensino, implementando uma plataforma web integrada que centraliza, automatiza e otimiza todo o ciclo de vida do programa de monitoria, desde a busca por ajuda até a gestão de dados para a melhoria contínua do serviço.
- **Público-Alvo**: 
  - Alunos: Estudantes que buscam apoio acadêmico para superar dificuldades em disciplinas específicas.
  - Monitores (Tutores): Alunos com bom desempenho que oferecem seu tempo para ensinar colegas, buscando experiência e remuneração.
  - Coordenação/Professores: Gestores acadêmicos e docentes responsáveis pelo recrutamento, supervisão e avaliação da eficácia do programa de monitoria.
- **Escopo**: O projeto consiste no desenvolvimento de uma aplicação web (Web App) que abrange as seguintes funcionalidades centrais:
  - Para Alunos: Consulta de monitores por disciplina, visualização de horários e agendamento de sessões.
  - Para Monitores: Gestão de agenda, registro de horas trabalhadas e comunicação com os alunos.
  - Para Coordenação: Publicação de vagas, gestão de candidaturas, validação de horas e acesso a um dashboard com relatórios básicos sobre a demanda e a oferta de monitorias.

---

### **3. Fases do Design Thinking**

#### **3.1. Empatia**

- **Pesquisa**: Para compreender o cenário, a análise do problema sugere a utilização de métodos de pesquisa qualitativa, como entrevistas com alunos, monitores e coordenadores para capturar suas frustrações e necessidades. Adicionalmente, a observação do processo atual e a análise de documentos (e-mails, planilhas de controle) para mapear a jornada de cada usuário.
- **Insights**: 
  - A falta de um canal centralizado gera ansiedade e desinformação, fazendo com que muitos alunos desistam de procurar ajuda.
  - Monitores gastam um tempo desproporcional com logística (agendar, remarcar, registrar horas) em vez de focar no ensino, o que causa desmotivação.
  - A gestão do programa opera "no escuro", sem métricas para entender quais disciplinas têm mais demanda ou para comprovar o valor do programa para a instituição.
  - O processo de candidatura para ser monitor é percebido como pouco transparente e desorganizado, desestimulando bons alunos a participarem.
- **Personas**: 
  - Mariana (Aluna): 19 anos, estudante de Engenharia. Sente-se sobrecarregada com a disciplina de Cálculo e não sabe a quem recorrer. Perde tempo procurando contatos de monitores em grupos de WhatsApp e se sente frustrada com a demora nas respostas para conseguir agendar uma aula.
  - Lucas (Monitor): 22 anos, estudante de Ciência da Computação e monitor de Algoritmos. É apaixonado por ajudar os outros, mas está exausto de gerenciar sua agenda manualmente, responder dezenas de mensagens e preencher relatórios de horas em planilhas separadas, sentindo que seu trabalho é mais burocrático do que pedagógico.
  - Prof.ª Cláudia (Coordenadora): 45 anos, coordenadora do curso. Acredita que a monitoria é fundamental, mas o processo de seleção de novos monitores é lento e baseado em trocas de e-mail. Ela não consegue responder a perguntas simples como "quantas horas de monitoria foram realizadas este mês?" ou "qual matéria teve mais procura?".

#### **3.2. Definição**

- **Problema Central**: Como podemos criar uma experiência de monitoria unificada e fluida que conecte alunos a monitores de forma simples, automatize as tarefas administrativas para os tutores e forneça dados estratégicos para a gestão do programa, fortalecendo o apoio acadêmico na instituição?
- **Pontos de Vista (POV)**: 
  - Para a Aluna: Mariana, uma estudante precisando de ajuda, necessita de uma forma rápida e confiável para encontrar e agendar monitorias, porque o método atual é fragmentado e gera incerteza, atrasando seu aprendizado.
  - Para o Monitor: Lucas, um monitor dedicado, precisa de uma ferramenta para automatizar o agendamento e o registro de suas atividades, porque o processo manual atual é cansativo e desvia o foco de sua principal tarefa: ensinar.
  - Para a Coordenadora: Prof.ª Cláudia, uma gestora acadêmica, precisa de visibilidade e dados consolidados sobre o programa, porque a falta de informações impede a otimização dos recursos e a tomada de decisões para melhorar o apoio oferecido aos alunos.

#### **3.3. Ideação**

- **Brainstorming**: 
- Para Alunos:
 - Um "catálogo" de monitores com filtros por disciplina, curso e horários.
 - Sistema de agendamento integrado a uma agenda online.
 - Avaliação e feedback (estrelas/comentários) para os monitores após a aula.
 - Notificações automáticas via app ou e-mail para lembrar das sessões.
 - Lista de espera para horários de monitores muito procurados.
- Para Monitores:
 - Painel de controle (dashboard) pessoal com agenda, próximos alunos e horas totais.
 - Ferramenta para definir e bloquear horários de disponibilidade facilmente.
 - Um chat interno para comunicação, separando-a do WhatsApp pessoal.
 - Registro de horas com "um clique" ao final de cada sessão, para aprovação do supervisor.
- Para Coordenação:
 - Portal para publicação e divulgação de vagas de monitoria.
 - Sistema digital para recebimento e comparação de candidaturas.
 - Dashboard com gráficos sobre as matérias mais procuradas e horas realizadas.
 - Funcionalidade para aprovar/reprovar horas registradas pelos monitores.
- **Seleção de Ideias**: As ideias foram priorizadas utilizando uma matriz de Impacto vs. Esforço. Foram selecionadas aquelas que atacavam diretamente as dores centrais de todos os usuários (alto impacto) e que poderiam ser desenvolvidas com um esforço razoável dentro do escopo de um projeto inicial (MVP - Mínimo Produto Viável).
- **Ideias Selecionadas**: 
 - Plataforma Centralizada de Agendamento: Unificar a busca por monitores, a visualização de perfis e a marcação de aulas em uma única interface. Resolve a dor principal da aluna Mariana e do monitor Lucas.
 - Módulo de Gestão de Candidaturas: Criar um portal para que a coordenação publique vagas e os alunos se candidatem online. Ataca diretamente a ineficiência do recrutamento sentida pela Prof.ª Cláudia.
 - Sistema Simplificado de Registro e Validação de Horas: Desenvolver uma ferramenta para que o monitor registre suas horas e a coordenação valide, automatizando a burocracia.
 - Dashboard de Gestão com Relatórios Iniciais: Painel para a coordenação com métricas essenciais (total de horas, monitores ativos, disciplinas com maior demanda).

#### **3.4. Prototipagem**

- **Descrição do Protótipo**: Foi desenvolvido um protótipo de alta fidelidade interativo. Ele consiste em telas navegáveis que simulam a experiência de uso da aplicação web em um navegador, sem a necessidade de programação de back-end. O protótipo foca nos três fluxos principais de uso:
 - Jornada do Aluno: Desde a busca por uma disciplina até a confirmação do agendamento.
 - Jornada do Monitor: Login, visualização da agenda e registro de uma sessão realizada.
 - Jornada da Coordenação: Visualização do dashboard principal e do processo de aprovação de horas.
- **Materiais Utilizados**: Para a criação do protótipo interativo, foi utilizada a ferramenta de design de interface Figma. Ícones, componentes de UI e guias de estilo foram criados para garantir consistência visual e uma experiência de usuário realista.
- **Testes Realizados**: O protótipo foi avaliado por alunos que tiveram acesso a versão beta.

#### **3.5. Teste**

- **Feedback dos Usuários**: O que os usuários acharam do protótipo.
- **Ajustes Realizados**: Mudanças feitas com base no feedback.
- **Resultados Finais**: Descrição da solução final.

---

### **4. Conclusão**

- **Resultados Obtidos**: O que foi alcançado com o projeto.
- **Próximos Passos**: O que ainda precisa ser feito ou implementado.
- **Aprendizados**: Lições aprendidas durante o processo.

---

### **5. Anexos**

- Fotos, gráficos, tabelas, transcrições de entrevistas, etc.

---

## **Dicas para Criar o Documento**

- Use uma linguagem clara e objetiva.
- Inclua visualizações, como mapas de empatia, jornadas do usuário ou esboços de ideias.
- Adapte o documento conforme o estágio do projeto (ex.: um documento inicial pode focar mais na pesquisa, enquanto um final pode detalhar a solução).

Esse modelo é flexível e pode ser ajustado conforme as necessidades do seu projeto ou da sua equipe. O importante é que o documento reflita o processo colaborativo e iterativo do Design Thinking.
