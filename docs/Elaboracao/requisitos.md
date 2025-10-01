# Especificação de Requisitos

## 1. Introdução
O documento descreve os requisitos do sistema Ibmec Monitoria, aplicativo voltado para gestão de sessões de monitoria acadêmica. Ele define o escopo, funcionalidades, restrições e regras de negócio, servindo como guia para o desenvolvimento e validação do sistema.

## 2. Visão Geral do Sistema
O Ibmec Monitoria tem como objetivo centralizar e simplificar o processo de monitoria acadêmica, permitindo interação entre alunos e monitores, agendamento de sessões, compartilhamento de materiais e acompanhamento do histórico.

Principais funcionalidades:

- Cadastro e autenticação de usuários (alunos, monitores e administradores).

- Agendamento e cancelamento de sessões.

- Aprovação ou recusa de agendamentos pelos monitores.

- Compartilhamento de materiais de estudo.

- Notificações via push/e-mail.

- Relatórios e histórico de monitorias.

Restrições:

- Disponível em web e mobile (Android/iOS).

- Necessário acesso à internet.

- Compatível com navegadores modernos e smartphones Android ≥ 9.0 e iOS ≥ 13.

## 3. Requisitos Funcionais

RF01 – Cadastro de Usuário: permitir que novos usuários realizem cadastro com nome, e-mail, senha e perfil de acesso. Um e-mail de confirmação deve ser enviado.

RF02 – Login e Autenticação: permitir login por e-mail e senha, utilizando tokens (JWT).

RF03 – Agendamento de Monitoria: permitir que alunos visualizem disponibilidade e solicitem sessões.

RF04 – Gerenciamento de Agendamentos: monitores podem aprovar ou recusar solicitações.

RF05 – Notificações: enviar notificações de confirmação, alteração ou cancelamento.

RF06 – Materiais de Apoio: monitores podem anexar materiais (PDFs, links, vídeos).

RF07 – Histórico de Sessões: permitir consulta ao histórico por alunos e monitores.

RF08 – Administração de Disciplinas: administradores podem cadastrar disciplinas e vincular monitores.

## 4. Requisitos Não Funcionais

RNF01 – Segurança: senhas devem ser criptografadas (bcrypt).

RNF02 – Desempenho: tempo de resposta inferior a 2 segundos.

RNF03 – Disponibilidade: sistema disponível 99% do tempo.

RNF04 – Usabilidade: interface responsiva, clara e adaptada a diferentes telas.

RNF05 – Portabilidade: compatível com Android ≥ 9, iOS ≥ 13 e navegadores modernos.

RNF06 – Escalabilidade: arquitetura deve suportar aumento de usuários sem perda significativa de desempenho.

## 5. Regras de Negócio

RN01 – Validação de Dados de Cadastro: e-mail deve ser único e válido.

RN02 – Recuperação de Senha: envio de link seguro para redefinição por e-mail.

RN03 – Perfis de Acesso:

Administrador: gerencia disciplinas, monitores e relatórios.

Monitor: aprova agendamentos, disponibiliza materiais e acompanha histórico.

Aluno: agenda sessões e acessa materiais.

## 6. Interfaces Externas
- API RESTful entre frontend e backend.

- Serviço de e-mail (SendGrid ou Gmail API).

- Firebase Cloud Messaging para notificações push.

- Banco de dados PostgreSQL para persistência.

## 7. Restrições
- Sistema não funciona offline.

- Apenas monitores cadastrados podem oferecer sessões.

- Upload de materiais limitado a 50 MB por arquivo.

## 8. Critérios de Aceitação
- Cadastro, login e agendamento devem funcionar em 95% dos testes.

- Notificações devem ser enviadas em até 10 segundos após eventos.

- Testes de usabilidade devem obter pelo menos 80% de aprovação dos usuários.

## 9. Glossário
Monitoria: atividade acadêmica de apoio.

Usuário: aluno, monitor ou administrador.

Sessão: encontro agendado presencial ou online.

Perfil de Acesso: nível de permissão no sistema.

## 10. Referências
Provost, F. & Fawcett, T. Data Science for Business: What You Need to Know about Data Mining and Data-Analytic Thinking. O’Reilly Media, 2013.

Han, J., Kamber, M., & Pei, J. Data Mining: Concepts and Techniques. Elsevier, 2011.

James, G., Witten, D., Hastie, T., & Tibshirani, R. An Introduction to Statistical Learning with Applications in R. Springer, 2013.

Documentação oficial do Python para Ciência de Dados: https://docs.python.org

Documentação do Pandas: https://pandas.pydata.org/docs

Documentação do Scikit-learn: https://scikit-learn.org/stable/

Documentação do PostgreSQL: https://www.postgresql.org

Documentação do Firebase: https://firebase.google.com/docs

Documentação do React Native: https://reactnative.dev