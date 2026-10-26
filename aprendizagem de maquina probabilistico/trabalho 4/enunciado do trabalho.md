# Trabalho 4

## Leia as instruções

- **O trabalho é individual.**
- **As implementações poderão ser realizadas em quaisquer linguagens de programação.**
- **Para a avaliação do trabalho, recomenda-se o envio de arquivo Jupyter notebook com os códigos executados e os resultados visíveis nas células.**

## 1. Probabilistic Principal Components Analysis (PPCA)

Implemente um modelo de **Probabilistic Principal Components Analysis (PPCA)** para os dígitos “5” do **dataset MNIST**, conforme disponibilizado no arquivo **mnist_5.csv**. O procedimento de treinamento deve ser feito via **algoritmo Expectation-Maximization (EM)**.

- O arquivo possui 6313 dígitos com 784 atributos (imagens com 28 × 28 pixels).
- Avalie o seu modelo nas tarefas de **reconstrução** e de **geração** de novas amostras.
- Experimente com diferentes valores para a dimensão do espaço latente (e.g. 2, 10, 20).

## 2. Inferência variacional

Considere os dados unidimensionais disponibilizados no arquivo **gaussian_1d.csv**. Implemente e execute um procedimento de **inferência variacional** para aproximar a posteriori dos parâmetros $\mu, \tau$ de uma Gaussiana univariada $\mathcal{N}(x \mid \mu, \tau^{-1})$ a partir desses dados.

- O arquivo possui 500 valores. Faça experimentos considerando somente os primeiros 10, 50, 100 pontos e, finalmente, todos os pontos.
- Indique o valor esperado da posteriori aproximada para os parâmetros $\mu, \tau$.
- Ilustre a aproximação obtida plotando as distribuições variacionais para $\mu, \tau$.