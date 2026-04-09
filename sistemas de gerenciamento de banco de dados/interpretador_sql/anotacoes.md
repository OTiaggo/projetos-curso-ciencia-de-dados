# Planejamento
1. Conferir se a consulta sql está correta
2. Transformar a conulta sql em um formato que eu consiga fazer as operações corretamente (uma árvore de operações)
3. Criar as funções para cada comando sql
4. Criar interface para o usuáiro


## Evolução
1. Fazer mais de uma consulta e retornar mais de uma resposta
2. Lidar com arquivos binários, não txt
3. Transformar em uma "API" de forma que eu possa usar esse sgbd em outro projeto


-----

# Rascunho
## Etapas de verificação do parser

| Categoria   | Pergunta de Validação                                                                 |
|-------------|---------------------------------------------------------------------------------------|
| Léxica      | Eu limpei espaços, vírgulas e ignorei o case (SELECT vs select)?                      |
| Sintática   | A ordem é obrigatoriamente SELECT -> COLUNAS -> FROM -> TABELA?                     |
| Semântica   | As colunas e a tabela existem no meu esquema?                                         |
| Lógica      | Se houver WHERE, ele tem os 3 elementos e o tipo de dado bate?                        |



## Todos os comandos sql

### DML (Data Manipulation Language) - Manipulação de Dados

- **SELECT:** Seleciona dados de uma tabela.
- **INSERT:** Insere novos dados.
- **UPDATE:** Atualiza dados existentes.
- **DELETE:** Apaga dados.

### DDL (Data Definition Language) - Definição da Estrutura

- **CREATE:** Cria novos bancos de dados ou tabelas.
- **ALTER:** Modifica estruturas existentes (ex: ALTER TABLE).
- **DROP:** Exclui tabelas ou bancos de dados.
- **TRUNCATE:** Remove todos os registros de uma tabela, mantendo sua estrutura.

### DCL (Data Control Language) - Controle de Acesso

- **GRANT:** Concede permissões aos usuários.
- **REVOKE:** Remove permissões de usuários.

### Cláusulas e Operadores Fundamentais

- **WHERE:** Filtra resultados com base em condições.
- **ORDER BY:** Ordena o resultado (ASC/DESC).
- **GROUP BY:** Agrupa linhas que têm os mesmos valores.
- **JOIN:** Combina linhas de duas ou mais tabelas.
- **LIKE:** Busca padrões em texto.

### Funções de Agregação

- **COUNT():** Conta o número de linhas.
- **SUM():** Soma valores.
- **AVG():** Calcula a média.
- **MAX() / MIN():** Encontra valores máximo/mínimo.
