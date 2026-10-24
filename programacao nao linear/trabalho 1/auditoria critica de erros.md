# Auditoria crítica de erros da IA

## 1. String mal delimitada no script auxiliar de geração da Parte 1

**Situação:** erro histórico, identificado e corrigido durante a preparação da Parte 1. **Local:** script auxiliar temporário que gerava as células do notebook; esse script não integra os arquivos de execução entregues.

**Solicitação relacionada:** preparar a fotografia e definir a função objetivo suave no notebook da Parte 1.

**Erro:** uma substituição redundante de barras invertidas nos textos LaTeX foi gerada com escape incorreto de barras e aspas. O script não pôde ser interpretado pelo Python.

**Como foi identificado:** a execução foi interrompida com o diagnóstico:

```text
SyntaxError: unterminated string literal (detected at line 94)
```

O traceback apontou a linha da substituição. A inspeção mostrou que o literal de texto não estava corretamente encerrado.

**Análise e correção:** em um literal comum de Python, uma barra invertida pode escapar a aspa seguinte, impedindo que ela encerre a string. Os textos matemáticos já eram escritos como strings brutas, de modo que a substituição adicional não era necessária. Foram removidas essas chamadas redundantes, preservando os comandos LaTeX no texto.

**Validação:** após a alteração, o script executou e o notebook foi gerado e executado com sucesso. Na revisão final, a Parte 1 voltou a executar integralmente, com as mesmas métricas. Esse episódio foi um bug de geração de código, sem evidência de erro nas fórmulas do modelo.

## 2. Omissão dos casos de uma função com gradiente nulo

**Situação:** encontrado e corrigido na revisão final. **Local:** `parte 2.ipynb`, função `executar_casos`, seção de execução das combinações.

**Solicitação relacionada:** implementar a Parte 2 e, posteriormente, verificar se havia erros nas duas partes.

**Erro:** a função `direcoes` sinalizava corretamente o gradiente numericamente nulo retornando uma lista vazia de direções. Entretanto, `executar_casos` percorria essa lista sem tratar o retorno vazio:

```python
g, H, itens = direcoes(funcao, x0)
for direcao in itens:
    # executar as combinações
```

Consequentemente, a função desaparecia dos resultados. Não havia um registro informando por que a busca não tinha sido realizada, e a matriz de 27 combinações ficava incompleta.

**Como foi identificado:** na revisão, o ponto inicial da TP 1 foi temporariamente alterado de `(8, 9)` para seu minimizador conhecido, `(5, 6)`, sem modificar os outros problemas. Antes da correção, o executor retornou **18 registros ao todo e nenhum da TP 1**, em vez de manter as 27 combinações com um diagnóstico explícito para as nove da TP 1.

**Análise que fundamenta a correção:**

$$f_1(u,v)=4(u-5)^2+(v-6)^2,$$

$$\nabla f_1(u,v)=(8(u-5),2(v-6))^T.$$

Em $(5,6)$, o gradiente é zero e o custo é zero. A direção de gradiente negativo é nula; como a Hessiana é definida positiva, as direções de Newton e Newton modificado também são nulas nesse ponto. Assim,

$$\phi(\alpha)=f_1((5,6)^T+\alpha\,0)=0$$

para qualquer passo. É impossível satisfazer uma redução estrita, e não existe uma direção de descida estrita a ser passada à busca. O comportamento correto é registrar o estado estacionário, sem procurar um passo artificial. Em outras funções, gradiente nulo não basta para concluir que o ponto é um mínimo; por isso o diagnóstico adotado é de **ponto estacionário**, sem declarar otimalidade global.

**O que foi feito para corrigir:** acrescentou-se um tratamento explícito para a lista de direções vazia. O executor agora preserva os nove registros da função, um para cada direção solicitada e método, com:

- `status = "estacionario"` e direção usada `nenhuma`;
- `alfa = 0`, ponto final igual ao inicial e custo final igual ao inicial;
- redução zero e nenhuma iteração de busca;
- condições de Goldstein não aplicáveis, representadas por `null` no JSON;
- contagem de uma avaliação do custo inicial por registro, sem avaliações de gradiente na linha;
- explicação de que nenhuma busca foi executada devido ao gradiente numericamente nulo.

As verificações de status passaram a distinguir `sucesso`, `estacionario` e `falha`. O cálculo de substituições de Newton conta apenas casos N → M, sem confundir ausência de direção com regularização.

**Validação:** o teste de regressão foi incluído no próprio notebook. Com TP 1 em `(5,6)`, confirmou **27 registros totais, nove estacionários da TP 1, passo zero, custo inalterado e nenhuma iteração de busca**. O ponto original foi restaurado em um bloco `finally`. O resultado dessa verificação está também em `resultados/parte2/experimentos.json`, no campo `verificacao_ponto_estacionario`.

Depois da correção, ambos os notebooks foram executados integralmente. Os resultados originais da Parte 1 e dos **27 casos obrigatórios e 27 extras da Parte 2 permaneceram idênticos** aos anteriores. O bug afetava a variação de entrada com gradiente nulo; os pontos padrão e extras originalmente entregues não acionavam esse caminho.

## 3. Quebra de linha inserida incorretamente no código de exportação da Parte 2

**Situação:** erro histórico, identificado e corrigido durante a implementação da Parte 2. **Local:** célula de exportação do resumo Markdown em `parte 2.ipynb`.

**Solicitação relacionada:** implementar a Parte 2, executar os experimentos e exportar os resultados.

**Erro:** ao construir o código da célula por meio de outra string Python, a sequência de quebra de linha foi interpretada uma camada antes do desejado. Uma quebra de linha real apareceu dentro de um literal curto da célula, tornando a instrução de gravação sintaticamente inválida.

**Como foi identificado:** a execução do notebook chegou à célula de exportação e foi interrompida com:

```text
SyntaxError: unterminated string literal (detected at line 33)
```

A inspeção da célula mostrada no traceback revelou o literal partido entre duas linhas na expressão de gravação de `resumo.md`.

**Análise e correção:** uma string curta delimitada por aspas não pode conter uma quebra de linha literal sem um mecanismo apropriado. Além disso, a geração de código dentro de outra string exigia considerar duas etapas de interpretação dos escapes. A correção evitou essa ambiguidade, usando o caractere de código 10 diretamente:

```python
(PASTA_SAIDA / "resumo.md").write_text(
    chr(10).join(texto), encoding="utf-8"
)
```

**Validação:** o notebook passou a executar a exportação, produzindo o resumo, os CSV e o JSON. A revisão final reexecutou a Parte 2 e confirmou a preservação dos resultados originais. O erro impedia a geração do resumo; não foi uma falha das derivadas ou das condições de Goldstein.

## Resultado e limites da revisão

- A Parte 1 foi reexecutada com **12 células de código**, e a Parte 2 com **13**, incluindo o teste de regressão acrescentado; não houve erros de execução.
- Foram feitas conferências adicionais por diferenças finitas em oito pontos regulares por função TP e em dados sintéticos de cores com dois valores de suavização. Os testes sustentaram as fórmulas implementadas nos pontos verificados; não constituem prova universal do código.
- Os 54 casos originais da Parte 2 continuam com redução estrita e as duas condições de Goldstein continuam satisfeitas nos casos desse método. As limitações de não convexidade e de um único passo permanecem explícitas.
- A ausência de descida de Newton clássico nas TP 8 e TP 15 padrão é uma propriedade matemática identificada e tratada conforme o enunciado, **não um erro produzido pela IA**.
- A perda de tons alaranjados na reconstrução da fotografia é uma limitação da paleta e do experimento, sem ser apresentada como bug ou como prova de melhora perceptual.
- O LaTeX não foi compilado nesta revisão, pois não foi localizado um compilador no ambiente. Portanto, não foi validada a diagramação de um PDF final. A atividade não foi enviada.

Os casos técnicos acima também foram incorporados ao apêndice do relatório, conforme a exigência de transparência do enunciado.
