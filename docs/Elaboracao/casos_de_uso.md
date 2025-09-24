---
id: diagrama_de_casos de uso
title: Diagrama de Casos de Uso
---

# Casos de Uso do App de Monitoria

---

## 1. Descrição dos Casos de Uso

| Categoria | Caso de Uso | Atores Principais |
| :--- | :--- | :--- |
| **Contas** | Criação de Conta | Aluno, Monitor, Coordenação |
| | Entrada (Login) | Aluno, Monitor, Coordenação |
| | Recuperação de Senha | Todos os usuários |
| | Visualização de Perfil | Todos os usuários |
| | Edição de Perfil | Todos os usuários |
| **Monitoria (Aluno)** | Buscar Monitor por Matéria | Aluno |
| | Agendar Horário com Monitor | Aluno, Monitor |
| | Avaliar Sessão de Monitoria | Aluno, Monitor |
| | Candidatar-se a Vaga de Monitoria | Aluno, Coordenação |
| **Monitoria (Monitor)** | Gerenciar Agenda de Disponibilidade | Monitor |
| | Aceitar/Recusar Solicitação de Agendamento | Monitor, Aluno |
| | Visualizar Histórico e Avaliações | Monitor |
| **Monitoria (Coordenação)** | Gerenciar Candidatos a Monitor | Coordenação |
| | Visualizar Relatórios e Métricas | Coordenação |

---

## 2. Detalhamento dos Casos de Uso

### 2.1. Criação de uma conta no sistema

**Atores:** Aluno, Monitor, Coordenação, Sistema

**Pré-Condições:** Nenhuma

**Fluxo Básico:**
1. O **Usuário** fornece e-mail, senha e confirmação de senha.
2. O **Sistema** valida os dados do usuário (formato, duplicidade de e-mail, segurança da senha).
3. O **Sistema** encripta a senha e persiste os dados do usuário.
4. O **Sistema** atribui o perfil inicial de **Aluno** ao novo usuário.
5. O **Sistema** exibe uma mensagem de sucesso.
6. O **Sistema** redireciona o usuário para a página de entrada.

**Fluxos Alternativos:**
* **2a. E-mail do usuário é inválido ou já está em uso:**
    * 2a1. O Sistema exibe mensagem de erro: "E-mail inválido" ou "E-mail já cadastrado".
* **2b. Senha do usuário não atende aos requisitos de segurança:**
    * 2b1. O Sistema exibe mensagem de erro.

### 2.2. Entrada (Login) do usuário no sistema

**Atores:** Aluno, Monitor, Coordenação, Sistema

**Pré-Condições:** O Usuário deve estar cadastrado.

**Fluxo Básico:**
1. O **Usuário** fornece e-mail e senha.
2. O **Sistema** autentica o usuário.
3. O **Sistema** redireciona o usuário para a página inicial, de acordo com seu perfil.
    * **Aluno:** Página de busca de monitores.
    * **Monitor:** Painel de gerenciamento de solicitações de agendamento.
    * **Coordenação:** Dashboard de relatórios.

**Fluxos Alternativos:**
* **2a. Dados de acesso incorretos:**
    * 2a1. O Sistema exibe mensagem de erro: "E-mail ou senha incorretos".

---

### 2.3. Buscar monitor por matéria

**Atores:** Aluno, Sistema

**Pré-Condições:** O Aluno deve estar logado no sistema.

**Fluxo Básico:**
1. O **Aluno** seleciona ou digita uma matéria na barra de busca.
2. O **Sistema** lista os monitores disponíveis para a matéria selecionada.
3. O **Aluno** visualiza os perfis dos monitores, incluindo informações como avaliações e agenda.

**Fluxos Alternativos:**
* **2a. Nenhúm monitor encontrado para a matéria:**
    * 2a1. O Sistema exibe uma mensagem informando que não há monitores disponíveis para a matéria selecionada.
* **3a. Aluno filtra a busca:**
    * 3a1. O Aluno aplica filtros adicionais (ex: por horário, por avaliação).
    * 3a2. O Sistema atualiza a lista de monitores com base nos filtros.

### 2.4. Agendar horário com monitor

**Atores:** Aluno, Monitor, Sistema

**Pré-Condições:** O Aluno deve estar logado. O Monitor deve ter disponibilidade cadastrada na agenda.

**Fluxo Básico:**
1. O **Aluno** seleciona um monitor da lista de busca.
2. O **Aluno** visualiza a agenda de disponibilidade do monitor.
3. O **Aluno** escolhe um horário vago e preenche os detalhes da sessão (ex: tópico).
4. O **Aluno** confirma a solicitação de agendamento.
5. O **Sistema** envia uma notificação para o monitor sobre a nova solicitação.
6. O **Monitor** recebe a notificação e pode aceitar ou recusar a solicitação.

**Fluxos Alternativos:**
* **4a. Horário selecionado já foi agendado por outro aluno (concorrência):**
    * 4a1. O Sistema informa o aluno que o horário não está mais disponível e sugere outro.
* **6a. Monitor recusa a solicitação:**
    * 6a1. O Sistema notifica o aluno sobre a recusa.

---

### 2.5. Candidatar-se a vaga de monitoria

**Atores:** Aluno, Sistema, Coordenação

**Pré-Condições:** O Aluno deve estar logado. A coordenação deve ter uma vaga aberta.

**Fluxo Básico:**
1. O **Aluno** navega para a seção de candidaturas.
2. O **Aluno** preenche o formulário de candidatura (ex: matéria, histórico, motivo do interesse).
3. O **Aluno** envia a candidatura.
4. O **Sistema** registra a candidatura e notifica a coordenação.
5. A **Coordenação** analisa a candidatura.
6. A **Coordenação** aprova ou rejeita a candidatura.
7. O **Sistema** notifica o aluno sobre o status da sua candidatura.

### 2.6. Gerenciar agenda de disponibilidade

**Atores:** Monitor, Sistema

**Pré-Condições:** O Monitor deve estar logado.

**Fluxo Básico:**
1. O **Monitor** acessa a seção de gerenciamento de agenda.
2. O **Monitor** define e atualiza seus dias e horários de trabalho (disponibilidade).
3. O **Monitor** salva as alterações na agenda.
4. O **Sistema** atualiza a agenda do monitor e a disponibiliza para os alunos.

**Fluxos Alternativos:**
* **2a. Monitor tenta remover a disponibilidade de um horário com agendamento confirmado:**
    * 2a1. O Sistema impede a alteração e exibe uma mensagem de erro.

### 2.7. Aceitar/recusar solicitação de agendamento

**Atores:** Monitor, Sistema, Aluno

**Pré-Condições:** O Monitor deve ter uma ou mais solicitações de agendamento pendentes.

**Fluxo Básico:**
1. O **Monitor** acessa o painel de solicitações.
2. O **Monitor** visualiza os pedidos pendentes (detalhes do aluno, horário).
3. O **Monitor** seleciona um pedido e escolhe **Aceitar** ou **Recusar**.
4. O **Sistema** atualiza o status do pedido.
5. O **Sistema** notifica o aluno sobre a decisão do monitor.
6. Se **Aceita**, o Sistema adiciona a sessão ao histórico do monitor e do aluno.

**Fluxos Alternativos:**
* **3a. Monitor não realiza a ação e a solicitação expira (timeout):**
    * 3a1. O Sistema cancela a solicitação automaticamente e notifica o aluno.

---

### 2.8. Gerenciar candidatos a monitor

**Atores:** Coordenação, Sistema

**Pré-Condições:** A Coordenação deve estar logada. Alunos devem ter submetido candidaturas.

**Fluxo Básico:**
1. A **Coordenação** acessa o painel de gerenciamento de candidatos.
2. A **Coordenação** visualiza e filtra a lista de candidaturas pendentes.
3. A **Coordenação** analisa a candidatura e seleciona **Aprovar** ou **Rejeitar**.
4. O **Sistema** atualiza o status da candidatura.
5. **Se Aprovada:** O Sistema altera o perfil do aluno para **Monitor** e o notifica.
6. **Se Rejeitada:** O Sistema notifica o aluno sobre a rejeição (com ou sem motivo).

### 2.9. Visualizar Relatórios e Métricas

**Atores:** Coordenação, Sistema

**Pré-Condições:** A Coordenação deve estar logada. Deve haver dados de monitoria registrados.

**Fluxo Básico:**
1. A **Coordenação** acessa o painel de relatórios (Dashboard).
2. O **Sistema** exibe gráficos e métricas essenciais.
    * Exemplos: Matérias mais demandadas, taxa de utilização do programa, horas totais de monitoria, média de avaliação dos monitores.
3. A **Coordenação** utiliza filtros (ex: por período, por matéria) para refinar a visualização.
4. O **Sistema** atualiza os dados conforme os filtros.