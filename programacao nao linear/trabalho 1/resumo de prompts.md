# Registro de prompts

Principais prompts e solicitações informados pelo estudante, com suas finalidades, para compor o apêndice de auditoria de IA do relatório final. O histórico inclui temas considerados antes da escolha da paleta de cores.

| Nº | Prompt ou solicitação | Finalidade |
| -- | -- | -- |
| 1 | “Me ajude a entender esse trabalho da faculdade.” | Interpretar o enunciado, identificar entregáveis e entender as etapas do projeto. |
| 2 | “Ainda não escolhi um problema para modelar. Faço Ciência de Dados. Retorne um Markdown com o planejamento inteiro do projeto e os to-dos.” | Organizar as atividades e adequar as sugestões à formação do estudante. |
| 3 | “Me ajude a escolher o problema real e obter seus dados ou parâmetros referenciados. Traga opções para eu escolher.” | Explorar temas com dados reais acessíveis. |
| 4 | “Me traga opções ligadas à otimização.” | Priorizar problemas com decisões explícitas de otimização. |
| 5 | “Localização de uma base de atendimento se encaixa bem no que preciso fazer neste trabalho?” | Avaliar a adequação do primeiro tema considerado aos requisitos da disciplina. |
| 6 | “Vou ficar com esse tema. Retorne um arquivo Markdown explicando o problema.” | Documentar a proposta inicial de localização de uma base. |
| 7 | “Prepare um arquivo AGENTS.md com tudo o que já foi decidido e feito até agora.” | Consolidar contexto, decisões, requisitos e pendências para continuidade do projeto. |
| 8 | “Me explique melhor como vou abordar o tema que escolhi.” | Compreender a relação entre dados, variáveis, função objetivo e busca linear. |
| 9 | “Eu preciso de dados reais para isso? Como consigo encontrar esses dados?” | Esclarecer a exigência de dados reais e localizar possíveis fontes públicas. |
| 10 | “Esse problema não é simples demais?” | Avaliar a profundidade matemática do tema e possíveis análises complementares. |
| 11 | “Não gostei das ideias de UAPS e escolas: queria aplicar ponderação e não considero realista um único ponto de abastecimento.” | Questionar as hipóteses operacionais e a justificativa dos pesos. |
| 12 | “Preciso de dados reais. Traga uma solução já com a fonte dos dados.” | Buscar uma aplicação com localização e demanda observadas. |
| 13 | “Essas vendas são de um comércio eletrônico específico?” | Verificar se a estrutura da base Olist sustentava a modelagem proposta. |
| 14 | “Desisti da ideia de minimizar a distância média. Sugira temas mais interessantes, focando na facilidade de obter dados reais.” | Redefinir o tema após avaliar as limitações das propostas anteriores. |
| 15 | “Não me interessei por nenhum; sugira mais.” | Ampliar a busca por aplicações de otimização. |


### Parte 1 — modelagem da paleta de cores

#### Pergunta para buscar trabalhos feitos relacionados ao problema

**Pergunta:** “Me indique artigos e pessoas que já fizeram essa modelagem.”

**Finalidade:** identificar trabalhos publicados que fundamentem a modelagem da paleta de cores. Foram indicados [**M. Emre Celebi (2011)**](https://arxiv.org/abs/1101.0395), pela quantização de cores por agrupamento, e [**Kenneth Rose (1998)**](https://scl.ece.ucsb.edu/sites/default/files/publications/b98_2_0.pdf), pela formulação suave de agrupamento usada como referência para o objetivo. Os links nos nomes levam aos artigos. A consulta busca o embasamento necessário para compreender e adaptar a modelagem.

Os itens da tabela abaixo são exemplos de prompts para estudo e pesquisa; não são transcrições de interações realizadas.

| Exemplo | Prompt sugerido | Finalidade |
| -- | -- | -- |
| P1.1 | “Explique como transformar os pixels da minha fotografia em uma matriz RGB normalizada. O que muda nos dados quando reduzo a resolução e como preservo a proporção da imagem?” | Entender a preparação dos dados e seus efeitos sobre o problema otimizado. |
| P1.2 | “Por que associar cada pixel diretamente à cor mais próxima pode gerar uma função não diferenciável? Explique a aproximação suave adotada e o efeito do parâmetro tau.” | Compreender a necessidade da suavização e a diferença entre o objetivo suave e o erro de reconstrução. |
| P1.3 | “Apresente a dedução do gradiente e dos blocos da Hessiana, explicando a regra da cadeia e por que os pesos de associação também dependem das cores da paleta.” | Estudar as derivadas analíticas e identificar termos que poderiam ser omitidos. |
| P1.4 | “Como posso conferir o gradiente e a Hessiana por diferenças finitas? Explique a escolha do passo numérico e como distinguir um erro de fórmula de um erro de aproximação.” | Planejar uma validação numérica das derivadas e interpretar suas limitações. |
| P1.5 | “A função suave da paleta é convexa? Explique a análise no ponto em que as três cores coincidem com a média dos pixels e a interpretação de uma direção de curvatura negativa.” | Discutir convexidade sem presumir que suavidade implica convexidade. |
| P1.6 | “Explique como conferir as duas condições de Goldstein no primeiro passo. A redução do objetivo suave garante que a fotografia reconstruída fique visualmente melhor?” | Verificar o critério de aceitação do passo e interpretar corretamente os resultados visuais. |
| P1.7 | “Pesquise referências sobre quantização de cores por agrupamento. Explique a relação entre o problema da paleta e o artigo Improving the Performance of K-Means for Color Quantization, de Celebi (2011).” | Estudar a base conhecida do problema e fundamentar sua contextualização com uma referência bibliográfica. |
| P1.8 | “Examine a formulação de energia livre de Rose (1998), na equação (25). Mostre como ela se relaciona ao objetivo deste trabalho ao usar pixels RGB, pesos 1/N, três cores com pesos 1/3 e temperatura fixa tau. Diferencie essa adaptação do algoritmo completo de deterministic annealing.” | Conferir a correspondência matemática com a referência e explicitar quais escolhas e simplificações pertencem ao recorte do trabalho. |

### Parte 2 — funções de teste e buscas lineares

| Exemplo | Prompt sugerido | Finalidade |
| -- | -- | -- |
| P2.1 | “Explique a construção do gradiente e da Hessiana das TP 8 e TP 15. Na TP 15, em quais pontos as derivadas não existem e como isso deve aparecer na implementação?” | Entender as derivadas e o tratamento de pontos não diferenciáveis. |
| P2.2 | “Como verificar se uma direção é de descida usando o produto entre o gradiente e a direção? Analise Newton clássico nos pontos iniciais das TP 8 e TP 15.” | Conferir os diagnósticos das direções antes de aplicar uma busca linear. |
| P2.3 | “Explique como escolher mu para que a Hessiana modificada seja definida positiva. Quando Newton e Newton modificado podem produzir a mesma direção?” | Justificar a regularização e evitar interpretar resultados coincidentes como erro. |
| P2.4 | “Explique a redução do intervalo na busca de Fibonacci, o reaproveitamento das avaliações e o tratamento da etapa final para evitar pontos coincidentes.” | Estudar os detalhes da implementação do método direto. |
| P2.5 | “Como construir e verificar os candidatos de interpolação quadrática e cúbica? Em quais situações uma salvaguarda deve substituir um candidato inadequado?” | Avaliar a estabilidade das interpolações e a preservação do intervalo de busca. |
| P2.6 | “Por que Goldstein pode precisar aumentar o passo, além de diminuí-lo? Use uma quadrática simples para mostrar como conferir as duas desigualdades.” | Entender e verificar as duas condições de aceitação em um caso conhecido. |
| P2.7 | “Como organizar as 27 combinações de maneira independente e comparar os métodos sem confundir avaliações de custo, avaliações de gradiente e diferenças nos critérios de parada?” | Planejar a leitura crítica das tabelas e das contagens de avaliações. |
| P2.8 | “O que o executor deve registrar quando o gradiente é nulo? Use a TP 1 em (5,6) para explicar por que não se deve exigir redução estrita nem omitir os casos.” | Compreender o erro identificado na revisão e verificar seu tratamento corrigido. |



