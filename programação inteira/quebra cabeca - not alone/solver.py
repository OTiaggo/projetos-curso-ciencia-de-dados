import pulp

def resolver_not_alone(tabuleiro_inicial):
    # Dimensão do tabuleiro
    n = len(tabuleiro_inicial)
    
    # 1. Cria o problema de otimização
    prob = pulp.LpProblem("Not_Alone_Solver", pulp.LpMinimize)
    
    # 2. Cria as variáveis binárias x_ij
    x = pulp.LpVariable.dicts("celula", ((i, j) for i in range(n) for j in range(n)), 
                              cat='Binary')
    
    # Função objetivo 
    prob += 0
    
    # 3. Restrições do problema
    
    # Restrição 1: Células originalmente preenchidas
    for i in range(n):
        for j in range(n):
            if tabuleiro_inicial[i][j] == 'A':
                prob += (x[i, j] == 1)
            elif tabuleiro_inicial[i][j] == 'Z':
                prob += (x[i, j] == 0)
                
    # Restrição 2: n/2 de "A" por linha
    for i in range(n):
        prob += (pulp.lpSum(x[i, j] for j in range(n)) == n // 2)
        
    # Restrição 3: n/2 de "A" por coluna
    for j in range(n):
        prob += (pulp.lpSum(x[i, j] for i in range(n)) == n // 2)
        
    # Restrições 4 e 5: Evitar "AZA" e "ZAZ"
    for i in range(n):
        for k in range(n - 2):
            # Linhas
            prob += (x[i, k] - x[i, k+1] + x[i, k+2] <= 1)  # Proíbe AZA
            prob += (x[i, k] - x[i, k+1] + x[i, k+2] >= 0)  # Proíbe ZAZ
            
    for j in range(n):
        for k in range(n - 2):
            # Colunas
            prob += (x[k, j] - x[k+1, j] + x[k+2, j] <= 1)  # Proíbe AZA
            prob += (x[k, j] - x[k+1, j] + x[k+2, j] >= 0)  # Proíbe ZAZ

    # 4. Loop para encontrar todas as soluções 
    solucoes = []
    
    while True:
        # Resolve o modelo
        prob.solve(pulp.PULP_CBC_CMD(msg=False))
        
        # Se não for mais viável, encontramos todas as soluções possíveis
        if pulp.LpStatus[prob.status] != "Optimal":
            break
            
        # Captura a solução atual
        solucao_atual = []
        for i in range(n):
            linha_str = ""
            for j in range(n):
                linha_str += "A" if pulp.value(x[i, j]) == 1 else "Z"
            solucao_atual.append(linha_str)
        solucoes.append(solucao_atual)
        
        # Criação do corte de exclusão para esta solução específica
        # Se na solução x_ij foi 1, queremos forçar que pelo menos uma variável mude
        corte = []
        for i in range(n):
            for j in range(n):
                if pulp.value(x[i, j]) == 1:
                    corte.append(1 - x[i, j])
                else:
                    corte.append(x[i, j])
                    
        # Pelo menos uma célula tem que ser diferente na próxima rodada
        prob += (pulp.lpSum(corte) >= 1)
        
    return solucoes

# --- Exemplo de teste usando o Exemplo 4 (6x6) do PDF ---
if __name__ == "__main__":
    tabuleiro_exemplo = [
        ['.', '.', '.', 'A', '.', '.'],  # Linha 1 (índice 0) -> ...A..
        ['.', '.', '.', '.', '.', '.'],  # Linha 2 (índice 1) -> ......
        ['.', '.', 'A', '.', 'A', '.'],  # Linha 3 (índice 2) -> ..A.A.
        ['A', '.', '.', '.', '.', '.'],  # Linha 4 (índice 3) -> A.....
        ['.', '.', '.', '.', '.', '.'],  # Linha 5 (índice 4) -> ......
        ['.', '.', '.', '.', '.', '.']   # Linha 6 (índice 5) -> ......
    ]
    
    resultado = resolver_not_alone(tabuleiro_exemplo)
    
    print(f"Total de soluções encontradas: {len(resultado)}")
    for idx, sol in enumerate(resultado, 1):
        print(f"\n--- Solução {idx} ---")
        for linha in sol:
            print(linha)