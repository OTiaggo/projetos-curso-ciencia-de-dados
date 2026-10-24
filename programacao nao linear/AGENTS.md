# AGENTS.md — Projeto de Programação Não Linear

## 1. Finalidade e estado deste documento

Este arquivo reúne o contexto, as decisões e o trabalho realizado até 24/10/2026 para que um agente de programação possa continuar o projeto sem recomeçar a discussão.

Leia este arquivo antes de implementar. Preserve as escolhas confirmadas pelo estudante, diferencie requisitos do professor de recomendações e atualize o andamento apenas com evidências do que foi efetivamente feito.

**Estado atual:** Partes 1 e 2 implementadas, executadas, documentadas e revisadas a pedido do estudante. A revisão identificou e corrigiu uma omissão de registros da Parte 2 em pontos estacionários. O teste de regressão agora preserva 27 registros, com nove estacionários da TP 1 em (5,6), sem busca artificial. Ambos os notebooks foram reexecutados sem erros, preservando os resultados originais da Parte 1 e dos 27 casos obrigatórios e 27 extras da Parte 2. A auditoria foi preenchida e incorporada ao relatório. A compilação LaTeX, a validação da diagramação do PDF e o envio da atividade permanecem pendentes. As seções sobre localização de uma base de atendimento abaixo são históricas.

### Tema atual — substitui a modelagem anterior

- **Problema:** representar uma fotografia com poucas cores, preservando o máximo possível de sua aparência.
- **Variáveis:** os valores RGB de três cores da paleta, totalizando nove componentes a otimizar.
- **Objetivo:** minimizar a diferença entre as cores dos pixels e sua representação pela paleta.
- **Dados escolhidos:** a fotografia local `nascer do sol rio de janeiro.jpeg`, indicada pelo estudante e com existência verificada. A própria fotografia é o dado de entrada; não é necessário coletar uma tabela externa.
- **Origem da fotografia:** fotografia tirada pelo próprio estudante, Tiago, conforme sua confirmação. Identificar no relatório e na legenda como **Fonte: acervo pessoal do autor**. O BSDS500 foi uma sugestão anterior; a imagem escolhida não foi obtida desse dataset. Não inventar data de captura ou outros detalhes não informados.
- **Recorte:** uma fotografia e uma paleta de três cores. A original tem 3024 × 4032 pixels; a versão de trabalho tem 192 × 256 pixels, com filtro LANCZOS e limite de 256 no maior lado, preservando a proporção. A matriz `pixels` tem formato `(49152, 3)`, com RGB em `float64` normalizado para `[0,1]`.
- **Adaptação:** o notebook define e implementa `objetivo_suave(x, pixels, tau)`, com $f_\tau(x)=-\frac{\tau}{N}\sum_i\log[\frac13\sum_{j=1}^3\exp(-\|p_i-c_j\|^2/\tau)]$. A avaliação usa deslocamento pelo mínimo das distâncias para estabilidade. Foi adotado $\tau=0{,}005$, fixo. Para o erro de associação à cor mais próxima $E$, vale $E\leq f_\tau\leq E+\tau\log 3$, com limite de aproximadamente 0,0054930614.
- **Domínio:** as nove variáveis são diretamente as componentes RGB em $\mathbb{R}^9$. Projetar uma paleta para o cubo RGB não aumenta as distâncias aos pixels nem o objetivo; por continuidade e compacidade, existe um minimizador global no cubo que também resolve o problema irrestrito. Não recortar as variáveis durante a otimização; passos intermediários podem sair do cubo. A função é suave e foi demonstrada não convexidade global por uma direção de curvatura negativa no ponto em que as cores coincidem com a média dos pixels. Na paleta inicial a Hessiana é numericamente definida positiva.
- **Apresentação:** comparar fotografia original, paleta inicial e imagem resultante. Distinguir o objetivo suave do erro da reconstrução por associação à cor mais próxima; a redução do primeiro não garante automaticamente melhora perceptual ou redução do segundo.
- **Derivadas e verificação:** gradiente e Hessiana deduzidos e implementados, incluindo a dependência dos pesos suaves na paleta. Diferenças finitas em duas paletas produziram erros absolutos máximos menores que 4,15e-11 no gradiente e 1,43e-9 na Hessiana.
- **Inicialização e passo:** cores de pixels nas posições 10%, 50% e 90% da ordenação por média RGB, sem algoritmo pronto de agrupamento. Direção $d_0=-g_0$ e Goldstein com $c=0{,}1$, tentativa inicial 1 e limite de 100 tentativas. O passo 1 foi aceito na primeira tentativa, satisfazendo ambas as condições; a paleta permaneceu no cubo sem recorte. Não foi executada otimização até convergência.
- **Resultados e limitações:** figuras e JSON em `resultados/parte1`; erro da associação à cor mais próxima caiu de 0,026729621032 para 0,024228079500. A comparação visual ainda perde os tons alaranjados do nascer do sol, limitação discutida no notebook e no relatório.
- **Parte 2 concluída:** TP 1, TP 8 e TP 15 com derivadas analíticas verificadas por diferenças finitas nos pontos padrão e em um ponto extra por função; direções G/N/M; Fibonacci, interpolação quadrática/cúbica com salvaguardas e Goldstein implementadas diretamente. Os 27 casos padrão e 27 extras produziram redução. CSV, JSON, resumo e gráficos estão em `resultados/parte2`.
- **Diagnósticos da Parte 2:** Newton clássico não fornece descida nas TP 8 e TP 15 padrão; suas três linhas por função usam M e preservam o diagnóstico original. Na TP 1, N e M coincidem com mu=0. Não contar essas linhas como trajetórias distintas nem como sucesso da direção clássica original.
- **Revisão final realizada:** corrigido o tratamento de gradiente numericamente nulo no executor da Parte 2, com registros de status `estacionario`, passo zero, custos inalterados e nenhuma busca. Não confundir estacionariedade com garantia de mínimo global. O teste de regressão está no notebook e seu resultado está no JSON. A auditoria contém esse caso e dois erros de sintaxe já resolvidos no desenvolvimento.
- **Próximo passo do projeto:** compilar o LaTeX e conferir a diagramação e os requisitos de envio quando solicitado. Não repetir nem ampliar as partes concluídas sem necessidade ou nova instrução.
- **Continuidade:** o tema de localização foi substituído. Não retomar dados geográficos, demanda ou TLC sem nova instrução. O planejamento e o documento de localização são históricos onde divergirem desta atualização.
- **Requisitos preservados:** a mudança afeta a modelagem da Parte 1; os testes TP 1, TP 8 e TP 15 e os métodos atribuídos da Parte 2 permanecem.

A Parte 1 foi executada integralmente e exportada, com um único passo de busca linear. A Parte 2 foi executada separadamente e incorporada ao relatório. A revisão conjunta solicitada foi realizada e a auditoria preenchida; não declarar que a compilação LaTeX, a validação da diagramação do PDF ou o envio já ocorreram.

## 2. Contexto acadêmico

- Estudante: Tiago.
- Curso: **Ciência de Dados**, Universidade Federal do Ceará.
- Disciplina: Programação Não Linear.
- Professor indicado no enunciado: Ricardo Coelho.
- Projeto: Primeiro Projeto Computacional — Modelagem e Busca Linear.
- Modalidade identificada no resultado do sorteio: **graduação individual**.
- Prazo indicado no PDF: **24 de outubro de 2026**. Horário e canal de envio não foram confirmados.
- Idioma de documentação e comunicação: português do Brasil.


## 3. Fontes e arquivos existentes

| Arquivo | Conteúdo e situação |
|---|---|
| `PNL_projeto_primeiro_20262 (1).pdf` | Fonte da descrição do trabalho enviada pelo professor; contém o enunciado e deve ser consultado para verificar os requisitos da atividade |
| `image(20261024-193541).png` | Captura do sorteio; confirma modalidade, TP 1, TP 8, TP 15 e métodos atribuídos |
| `planejamento_projeto_pnl.md` | Planejamento geral criado, com tarefas, matriz de experimentos e orientações de entrega; contém trechos anteriores à escolha do tema |
| `modelagem_localizacao_base_atendimento.md` | Descrição criada após a escolha do tema; contém objetivo, formulação, derivadas, convexidade, hipóteses e pendências |
| `AGENTS.md` | Consolidação atual do contexto e das decisões |
| `no que a IA ajudou.md` | Registro do que a IA já ajudou no trabalho, para constar no relatório final |
| `resumo de prompts.md` | Registro dos principais prompts e solicitações feitos à IA, com suas finalidades, para compor o apêndice de auditoria de IA exigido no enunciado |
| `auditoria critica de erros.md` | Registro crítico a ser preenchido na revisão final das duas partes, quando solicitada pelo estudante, com os erros reais encontrados, evidências, identificação, correção fundamentada e validação, para compor o apêndice de auditoria de IA |
| `relatorio entregavel latex.md` | Arquivo que conterá o relatório final do trabalho |
| `relatorio.tex` | Fonte LaTeX de entrega, enxugada a pedido do estudante para concentrar os requisitos do professor; contém as duas partes, as tabelas dos 27 casos, manual unificado e auditoria. A seção de responsabilidades foi removida a pedido do estudante. A compilação ainda não foi verificada |
| `parte 1.ipynb` | Notebook que conterá todos os códigos da Parte 1: modelagem da paleta de três cores para a fotografia escolhida; anteriormente chamado `codigos.ipynb` |
| `testar_paleta.ipynb` | Notebook independente de teste, convertido da aplicação Python a pedido do estudante; contém upload via ipywidgets, reconstrução e saída RGB/HEX, sem importar arquivo Python externo |
| `como testar a paleta.md` | Instruções de instalação, abertura e uso do notebook de teste |
| `parte 2.ipynb` | Notebook que conterá todos os códigos da Parte 2: experimentos TP 1, TP 8 e TP 15, direções e métodos de busca linear atribuídos |
| `nascer do sol rio de janeiro.jpeg` | Fotografia tirada pelo estudante, Tiago, escolhida como entrada da modelagem de paleta de três cores; fonte: acervo pessoal do autor |

Os nomes são referências portáveis: ao receber este arquivo em outro ambiente, localizar os documentos no projeto. Não presumir que os caminhos temporários da conversa existem nessa máquina.

### Como resolver informações desatualizadas

- A escolha mais recente é a paleta de três cores; instruções sobre localização no planejamento antigo e neste histórico foram substituídas.
- No planejamento antigo, afirmações como “modelagem ainda não escolhida” e sugestões de regressão deixaram de representar o estado atual.
- Não voltar à seleção de tema nem adotar regressão linear, regressão logística ou Auto MPG como modelagem sem uma nova instrução do estudante.
- Se for solicitado atualizar o planejamento geral, alinhar suas seções antigas ao tema de paleta de cores e ao estado concluído da Parte 1.
- Consultar o enunciado original para esclarecer exigências; não elevar recomendações deste arquivo a obrigações da disciplina.

## 4. Decisões do tema anterior — histórico substituído pelo tema atual

1. A modelagem real será **localização de uma única base de atendimento**.
2. A decisão será a posição da base em um plano, com duas coordenadas contínuas.
3. O objetivo será minimizar distâncias ponderadas pela demanda.
4. A formulação documentada utiliza distância euclidiana suavizada para permitir gradiente e Hessiana em todo o domínio.
5. O problema será tratado como irrestrito em $\mathbb{R}^2$, com limitações físicas explicitadas.
6. A modelagem é a Parte 1 e não substitui os experimentos obrigatórios da Parte 2.
7. O estudante solicitou documentos Markdown para registrar o planejamento e a explicação do tema; ambos foram criados.

**Título de trabalho:** Localização de uma base de atendimento por minimização de distâncias ponderadas pela demanda.

## 5. Requisitos obrigatórios do projeto

### Parte 1 — Uma modelagem real

- Contextualizar o problema e apresentar dados reais ou parâmetros físicos referenciados, com unidades.
- Definir o vetor de decisão.
- Formular uma função objetivo irrestrita, eliminando ou tratando restrições conforme o enunciado.
- Deduzir analiticamente o gradiente e a Hessiana.
- Discutir convexidade.
- Escolher um ponto inicial plausível, usar a direção do gradiente negativo e aplicar um dos métodos implementados.
- Comprovar numericamente uma redução do objetivo no primeiro passo.

Não se exige convergência final completa da modelagem.

### Parte 2 — Testes atribuídos

- Funções: **TP 1, TP 8 e TP 15**, com os pontos iniciais do catálogo.
- Direções: gradiente negativo, Newton clássico e Newton modificado.
- Métodos: **Fibonacci, interpolação quadrática/cúbica e condições de Goldstein**.
- Total: **3 funções × 3 direções × 3 métodos = 27 combinações**.
- O foco é determinar o passo na direção e apresentar o próximo ponto, não executar obrigatoriamente 27 otimizações completas.
- Os casos partem dos pontos iniciais indicados, de maneira independente; não encadear métodos como se fossem passos sucessivos de uma mesma execução.
- Verificar se cada direção é de descida. Registrar falhas de Newton e aplicar a regularização prescrita.

### Entrega

- Descrição da modelagem, derivadas, convexidade e primeiro passo.
- Relatório dos experimentos com análise dos resultados.
- Manual de uso **dentro do relatório**; um README isolado não basta.
- Código-fonte comentado, implementando os métodos sem usar uma caixa-preta de busca unidimensional em seu lugar.
- Apêndice de auditoria de IA.
- A discriminação formal de tarefas por integrante é obrigatória para duplas. Aqui, a modalidade é individual; identificar a autoria conforme a estrutura de entrega.
- Testes em outros pontos iniciais são recomendados para robustez, sem substituir os casos obrigatórios.

## 6. Formulação do tema anterior — histórico, não usar no tema atual

### Contexto

Uma organização atende solicitações em diferentes locais. Deseja posicionar uma base para reduzir o deslocamento geométrico até esses locais. Regiões com maior demanda devem ter maior influência.

Não foi escolhida ainda uma organização, cidade ou aplicação operacional específica. Central de assistência técnica e ponto de apoio são exemplos, não decisões definitivas.

### Dados e variáveis

- $p_i=(a_i,b_i)^T$: posição fixa do ponto ou região atendida.
- $n_i$: quantidade de solicitações no período selecionado.
- $w_i>0$: peso de demanda.
- $x=(u,v)^T\in\mathbb{R}^2$: posição da base, que será otimizada.
- $\varepsilon>0$: parâmetro de suavização, na mesma unidade das coordenadas.

Considerar um conjunto finito não vazio de pontos com demanda positiva. Converter coordenadas geográficas para um sistema plano adequado à região, em metros ou quilômetros. Não calcular a distância euclidiana diretamente em graus de latitude e longitude.

Pesos normalizados são uma opção documentada:

$$w_i=\frac{n_i}{\sum_j n_j}.$$

Usar contagens $w_i=n_i$ também é possível. Isso muda a escala do objetivo e do gradiente, embora preserve o minimizador. A convenção final ainda não foi escolhida.

### Objetivo

$$r_i(x)=\sqrt{\|x-p_i\|^2+\varepsilon^2},\qquad f(x)=\sum_{i=1}^{m}w_i r_i(x).$$

Resolver:

$$\min_{x\in\mathbb{R}^2}f(x).$$

É uma aproximação suave da soma de distâncias. Não substituir silenciosamente por distâncias quadráticas: isso altera o problema.

Para a distância exata $d_i=\|x-p_i\|$, vale $0\leq r_i-d_i\leq\varepsilon$. Se $\sum_iw_i=1$, o erro no valor do objetivo fica limitado por $\varepsilon$. Esse limite não é um limite para a diferença entre as posições minimizadoras.

### Derivadas já documentadas

Com $z_i=x-p_i$:

$$\nabla f(x)=\sum_i w_i\frac{z_i}{r_i},$$

$$\nabla^2f(x)=\sum_i w_i\left(\frac{I}{r_i}-\frac{z_i z_i^T}{r_i^3}\right).$$

Essas fórmulas já constam analiticamente no documento de modelagem. Ainda precisam ser implementadas e verificadas numericamente.

### Convexidade já discutida

Para $h\neq0$:

$$h^T\nabla^2f(x)h\geq\sum_i\frac{w_i\varepsilon^2}{r_i^3}\|h\|^2>0.$$

Logo, a Hessiana é definida positiva em todo o plano e a função é estritamente convexa. Como a função é coerciva, existe um único minimizador global.

Não afirmar convexidade forte uniforme em todo $\mathbb{R}^2$: os menores autovalores podem se aproximar de zero longe dos pontos.

### Primeiro passo ainda pendente

1. Escolher $x^{(0)}$ plausível com gradiente numericamente não nulo.
2. Calcular $d_0=-\nabla f(x^{(0)})$.
3. Construir $\phi(\alpha)=f(x^{(0)}+\alpha d_0)$.
4. Aplicar um dos três métodos implementados para obter $\alpha_0>0$.
5. Calcular $x^{(1)}$ e comprovar $f(x^{(1)})<f(x^{(0)})$.

Não há valores numéricos definidos para $\varepsilon$, ponto inicial ou passo.

### Hipóteses e limitações a preservar

- Uma única base, com demanda fixa no período considerado.
- Distância geométrica, sem modelagem de vias, congestionamento ou tempo de viagem.
- Deslocamentos base–ponto; não há otimização de rotas com várias paradas.
- Se as viagens forem sempre de ida e volta simétricas, multiplicar o objetivo por dois não altera o minimizador.
- Localização contínua: disponibilidade de imóveis, zoneamento e barreiras físicas ficam fora do modelo inicial.
- Se forem usados centroides, declarar que eles aproximam a localização interna da demanda.
- O resultado é apoio preliminar à decisão, não uma garantia de viabilidade operacional.

## 7. Dados do tema anterior — histórico, não usar no tema atual

Foi sugerida a fonte pública NYC Taxi & Limousine Commission (TLC):

- Página: https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page
- A página foi consultada na conversa e disponibiliza registros de viagens e arquivos geográficos de zonas.
- Uma proposta é contar embarques por zona como peso e representar as zonas por centroides.
- Isso corresponderia a uma **base de apoio à demanda de transporte**; não tratar embarques como solicitações reais de assistência técnica sem justificar essa adaptação.
- A fonte é apenas candidata: o estudante não confirmou Nova York, TLC ou qualquer período.
- Os dados geográficos e de demanda dessa fonte ainda não foram baixados nem preparados.

Não presumir Fortaleza como área de estudo apenas por informações pessoais. A escolha geográfica está aberta.

Uma exploração anterior de temas de previsão consultou Auto MPG, Bike Sharing, Student Performance e Wine Quality. Essas bases **não foram escolhidas para a modelagem atual**. Houve download exploratório do ZIP Auto MPG, sem adoção no projeto. Não contabilizar isso como obtenção dos dados necessários à localização.

## 8. Funções de teste: fórmulas e cuidados

### TP 1 — Grupo 1

$$f_1(x)=4(x_1-5)^2+(x_2-6)^2,\qquad x^{(0)}=(8,9)^T.$$

- Gradiente: $(8(x_1-5),\;2(x_2-6))^T$.
- Hessiana: $\operatorname{diag}(8,2)$.
- Mínimo de referência: $(5,6)^T$, valor zero.
- Útil para validar direções e passos com cálculo analítico.

### TP 8 — Grupo 2

$$f_8(x)=[1{,}5-x_1(1-x_2)]^2+[2{,}25-x_1(1-x_2^2)]^2+[2{,}625-x_1(1-x_2^3)]^2,$$

$$x^{(0)}=(0,0)^T.$$

Alerta analítico já registrado, a validar na implementação:

$$g_0=(-12{,}75,0)^T,\qquad H_0=\begin{pmatrix}6&3\\3&0\end{pmatrix},\qquad d_N=(0,4{,}25)^T.$$

Nessa direção, $g_0^Td_N=0$ e a função permanece constante porque $x_1=0$ ao longo da linha. **Newton clássico não é direção de descida estrita nesse caso.** Registrar a falha e aplicar Newton modificado conforme o enunciado.

### TP 15 — Grupo 3

$$f_{15}(x)=\left[10(x_1-x_2^2)^2+(x_1-1)^2\right]^{1/4},\qquad x^{(0)}=(-1{,}2;1{,}0)^T.$$

- A potência $1/4$ se aplica à soma inteira.
- Atenção à regra da cadeia no gradiente e na Hessiana.
- A expressão interna se anula em $(1,1)$ e $(1,-1)$; a função não é diferenciável nesses pontos.
- Não avaliar fórmulas de derivadas com potências negativas da expressão interna quando ela for zero.
- Não assumir definitude positiva da Hessiana apenas pelo grupo atribuído à função.

As derivadas gerais de TP 8 e TP 15 foram implementadas e verificadas por diferenças finitas no `parte 2.ipynb`. Os erros escalados máximos entre todas as funções/pontos foram menores que 1,1e-10 para o gradiente e 8,6e-11 para a Hessiana.

## 9. Regras de implementação e comparação

### Direções

Com $g=\nabla f(x^{(0)})$ e $H=\nabla^2f(x^{(0)})$:

$$d_G=-g,\qquad Hd_N=-g,\qquad(H+\mu I)d_M=-g.$$

- Resolver sistemas lineares em vez de formar explicitamente inversas.
- Garantir $\mu\geq0$ e $H+\mu I\succ0$. A regra adotada é $\delta=\max(10^{-6},10^{-2}\max(1,\max_i|\lambda_i(H)|))$ e $\mu=\max(0,\delta-\lambda_{\min}(H))$, com conferência por Cholesky.
- Verificar $g^Td<0$ antes da busca, com tratamento explícito de tolerâncias e gradiente nulo.
- Quando Newton falhar, preservar o diagnóstico da direção original e registrar a direção regularizada efetivamente utilizada.
- $\mu=0$ é permitido quando $H$ já é definida positiva; Newton e Newton modificado podem coincidir. Não forçar diferenças artificiais.

### Buscas

- **Fibonacci:** implementar redução de intervalo, seleção do número de etapas e reaproveitamento de avaliações; tratar os pontos coincidentes da etapa final.
- **Interpolação:** foi implementada uma busca que alterna candidatos quadráticos e cúbicos de Hermite, com atualização do vale e salvaguarda por ponto médio quando o candidato é inadequado. Ambas as variantes estão na mesma busca por combinação, mantendo o total obrigatório de 27 casos. Contar as avaliações adicionais de gradiente do cúbico separadamente.
- **Goldstein:** para $0<c<1/2$, implementar ambas as condições:

$$\phi(0)+(1-c)\alpha\phi'(0)\leq\phi(\alpha)\leq\phi(0)+c\alpha\phi'(0).$$

- Goldstein pode exigir expansão ou redução do passo; simples redução sucessiva pode não satisfazer a condição inferior.
- Métodos em intervalo precisam de um procedimento documentado de obtenção do intervalo. Para funções não convexas, não prometer mínimo global sem justificar as hipóteses.
- Implementar limites de iterações, verificação de valores não finitos e motivos de parada.
- Não usar `minimize_scalar`, buscas prontas ou equivalentes para substituir os três algoritmos pedidos.
- Os códigos estão em Python nos dois notebooks; NumPy é usado para álgebra linear e Matplotlib para figuras. As derivações são analíticas e as conferências usam diferenças finitas, sem depender de um motor simbólico na execução.

### Registro dos experimentos

Registrar, por combinação: TP, ponto inicial, método, parâmetros, direção solicitada/usada, $\mu$, $g^Td$, intervalo quando aplicável, passo, próximo ponto, valores antes/depois, redução, iterações, avaliações e status.

Para Goldstein, registrar a verificação das duas desigualdades. Se houver substituição da direção de Newton, contabilizar os casos atribuídos com o diagnóstico e a substituição; não fingir que houve sucesso da direção clássica nem fabricar trajetórias distintas para chegar a 27.

## 10. Histórico inicial de trabalho — tema anterior

- [x] Ler o enunciado e a imagem do sorteio.
- [x] Identificar modalidade, funções, métodos e quantidade de experimentos.
- [x] Explicar a diferença entre direção e comprimento do passo.
- [x] Criar `planejamento_projeto_pnl.md`.
- [x] Apresentar alternativas de temas e fontes públicas candidatas.
- [x] Confirmar com o estudante o tema de localização de uma base de atendimento.
- [x] Definir e explicar a formulação suave de duas variáveis.
- [x] Documentar gradiente, Hessiana e argumento de convexidade da modelagem.
- [x] Criar `modelagem_localizacao_base_atendimento.md`.
- [x] Consolidar o histórico e as pendências neste `AGENTS.md`.

**Situação histórica do tema anterior:** a modelagem de localização foi abandonada antes de obter dados e implementar seus algoritmos. Para o estado atual da Parte 1 de paleta de cores, consultar a seção 1.

## 11. Próximas tarefas, em ordem sugerida

- [x] Escolher a fotografia: `nascer do sol rio de janeiro.jpeg`.
- [x] Confirmar origem e autoria da fotografia: tirada pelo estudante, Tiago, de seu acervo pessoal.
- [x] Identificar a fotografia no relatório e na legenda como fonte: acervo pessoal do autor.
- [x] Definir resolução, conversão para RGB e escala dos componentes.
- [x] Formular e implementar o objetivo suave e justificar os limites RGB no problema irrestrito.
- [x] Deduzir gradiente e Hessiana e discutir convexidade do novo modelo.
- [x] Definir e justificar o parâmetro de suavização e a paleta inicial.
- [x] Usar Python e organizar os códigos nos notebooks de cada parte.
- [x] Escolher e documentar a variante de interpolação na Parte 2.
- [x] Implementar objetivo, gradiente e Hessiana da Parte 1 e verificar por diferenças finitas.
- [x] Implementar objetivos, gradientes e Hessianas das funções TP da Parte 2 e validar derivadas.
- [x] Implementar direções, regularização e diagnóstico de descida.
- [x] Implementar e validar Fibonacci, interpolação e Goldstein em casos simples.
- [x] Executar os 27 casos obrigatórios e 27 extras e exportar resultados reproduzíveis.
- [x] Executar o primeiro passo da modelagem real e comprovar redução.
- [x] Produzir visualizações e discutir resultados e limitações da Parte 1.
- [x] Redigir a Parte 1 do relatório, com manual e auditoria de IA.
- [x] Completar o relatório e manual com os resultados da Parte 2.
- [x] Preencher a auditoria crítica na revisão conjunta final solicitada pelo estudante.
- [x] Revisar fórmulas e implementação, reexecutar os notebooks e conferir a consistência dos resultados com o relatório e o enunciado.
- [ ] Compilar o LaTeX, conferir diagramação do PDF e requisitos de envio.

O estudante deve poder entender as escolhas. Explicar o que cada etapa resolve e preservar a rastreabilidade dos resultados.

## 12. Organização de código sugerida, ainda não implementada

```text
src/problems.py       # funções de teste e derivadas
src/modeling.py       # paleta de cores e dados da imagem
src/directions.py     # direções e regularização
src/line_search.py    # os três métodos
src/experiments.py    # execução e exportação
data/                # dados e documentação de origem
results/             # resultados e figuras gerados
report/              # relatório e auditoria de IA
requirements.txt     # dependências, se Python for adotado
README.md            # instruções resumidas
```

Essa estrutura é recomendação, não um repositório já criado nem uma exigência do professor.

Conforme definido pelo estudante, todos os códigos da Parte 1 devem ficar no notebook `parte 1.ipynb` e todos os códigos da Parte 2 devem ficar no notebook `parte 2.ipynb`. O antigo `codigos.ipynb` foi renomeado para `parte 1.ipynb`. A estrutura de módulos acima é apenas uma sugestão anterior; priorizar a organização nos dois notebooks solicitados.

Posteriormente, o estudante solicitou uma ferramenta de teste separada do notebook da Parte 1 e pediu sua conversão para notebook. Essa exceção está em `testar_paleta.ipynb`, com upload de imagens via ipywidgets, prévia da reconstrução e saída RGB/HEX. O arquivo é autônomo e substitui a antiga aplicação `testar_paleta.py`, sem Tkinter. Usa o objetivo, a inicialização e um passo de Goldstein da Parte 1, com tratamento adicional de imagens com poucas cores, gradiente nulo e transparência. A fotografia do trabalho reproduz os resultados originais; a ferramenta não altera as saídas dos experimentos.

## 13. Auditoria de IA e integridade dos resultados

Manter o arquivo `no que a IA ajudou.md` atualizado com as contribuições efetivamente realizadas pela IA, para que esse histórico conste no relatório final. O arquivo `relatorio entregavel latex.md` conterá o relatório final do trabalho.

Manter `resumo de prompts.md` com os principais prompts e solicitações feitos à IA e a finalidade de cada um. Os registros iniciais foram fornecidos pelo estudante e incluem a exploração de temas anteriores; preservar esse histórico sem confundi-lo com o tema atual.

O documento `auditoria critica de erros.md` deve relatar **pelo menos uma situação real em que o modelo gerou formulações equivocadas, derivadas parciais incorretas ou bugs de implementação**, como laços infinitos na busca linear ou violação da condição de descida, e explicar **como o erro foi identificado e corrigido analiticamente**, conforme o enunciado do professor.

Esses dois arquivos fornecem o material para a seção/apêndice de auditoria de IA de `relatorio entregavel latex.md`; sua existência isolada não substitui a inclusão desse conteúdo no relatório final. O arquivo `no que a IA ajudou.md` continua sendo o resumo das contribuições da IA.

O enunciado permite e incentiva o uso de IA, exigindo:

1. Resumo dos principais prompts.
2. Pelo menos uma situação real de erro produzido pela IA, com identificação e correção fundamentadas.

- Guardar os pedidos relacionados a planejamento, seleção do tema, formulação e implementação.
- Não inventar erros, dados, parâmetros referenciados ou resultados para completar o relatório.
- Alertas preventivos sobre TP 8, TP 15 e Goldstein não são evidências de erros efetivamente cometidos.
- Foi documentado um erro técnico real no script auxiliar de geração do notebook: `SyntaxError: unterminated string literal (detected at line 94)`, por escape incorreto de barras/aspa em substituição redundante. A correção removeu a substituição dos textos já brutos; a execução posterior do notebook validou a correção. O incidente está no relatório e no registro da ajuda da IA. Não é um erro observado na formulação ou na rotina de Goldstein; não inventar um incidente matemático.
- Não declarar que uma fórmula foi validada computacionalmente se apenas foi escrita ou discutida.

## 14. Critério de continuidade

As Partes 1 e 2 estão concluídas e foram revisadas mediante solicitação do estudante. A auditoria foi preenchida com um bug de registro de pontos estacionários encontrado e corrigido na revisão e dois erros de sintaxe históricos já corrigidos. A Parte 2 mantém os 27 casos obrigatórios e 27 extras originais, com os diagnósticos de substituição de Newton preservados. Restam a compilação LaTeX, a conferência visual do PDF e os requisitos de envio; não afirmar que essas etapas ocorreram. O tema de localização foi substituído; as instruções atuais da seção 1 prevalecem sobre o histórico.
