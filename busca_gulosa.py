import heapq

# =============================================================================
# DATASET: Mapa da Roménia (Baseado no livro de Russell & Norvig)
# =============================================================================

# 1. Definição do Grafo (Conexões reais e estradas entre as cidades)
grafo = {
    'Arad': ['Zerind', 'Sibiu', 'Timisoara'],
    'Zerind': ['Arad', 'Oradea'],
    'Oradea': ['Zerind', 'Sibiu'],
    'Sibiu': ['Arad', 'Oradea', 'Fagaras', 'Rimnicu Vilcea'],
    'Fagaras': ['Sibiu', 'Bucareste'],
    'Rimnicu Vilcea': ['Sibiu', 'Craiova', 'Pitesti'],
    'Craiova': ['Drobeta', 'Rimnicu Vilcea', 'Pitesti'],
    'Drobeta': ['Mehadia', 'Craiova'],
    'Mehadia': ['Lugoj', 'Drobeta'],
    'Lugoj': ['Timisoara', 'Mehadia'],
    'Timisoara': ['Arad', 'Lugoj'],
    'Pitesti': ['Rimnicu Vilcea', 'Craiova', 'Bucareste'],
    'Bucareste': ['Fagaras', 'Pitesti', 'Giurgiu', 'Urziceni']
}

# 2. Valores da Heurística h(n): Distância em linha reta até Bucareste
heuristica = {
    'Arad': 366, 'Bucareste': 0, 'Craiova': 160, 'Drobeta': 242, 
    'Eforie': 161, 'Fagaras': 176, 'Giurgiu': 77, 'Hirsova': 151, 
    'Iasi': 226, 'Lugoj': 244, 'Mehadia': 241, 'Neamt': 234, 
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193, 
    'Sibiu': 253, 'Timisoara': 329, 'Urziceni': 80, 'Vaslui': 199, 
    'Zerind': 374
}

# =============================================================================
# ALGORITMO: Busca Gulosa (Greedy Best-First Search)
# =============================================================================

def busca_gulosa(origem, destino):
    """
    Executa a busca gulosa a partir de uma cidade de origem até ao destino.
    A prioridade da borda é definida estritamente pela função heurística h(n).
    """
    # Fila de prioridade (borda): armazena tuplas (valor_heuristica, cidade_atual, caminho_percorrido)
    borda = []
    heapq.heappush(borda, (heuristica[origem], origem, [origem]))
    
    # Conjunto para evitar ciclos e estados repetidos (Busca em Grafo)
    visitados = set()
    
    print(f"Iniciando busca de '{origem}' para '{destino}':\n")
    
    while borda:
        # Extrai o nó com a MENOR estimativa heurística h(n)
        h_atual, cidade_atual, caminho = heapq.heappop(borda)
        
        print(f" -> Expandindo: {cidade_atual} (h = {h_atual})")
        
        # Teste de objetivo
        if cidade_atual == destino:
            print("\n[Sucesso] Objetivo alcançado!")
            return caminho
            
        if cidade_atual not in visitados:
            visitados.add(cidade_atual)
            
            # Gerar sucessores/vizinhos
            for vizinho in grafo.get(cidade_atual, []):
                if vizinho not in visitados:
                    # Na busca gulosa, a prioridade depende EXCLUSIVAMENTE de h(vizinho)
                    prioridade = heuristica[vizinho]
                    heapq.heappush(borda, (prioridade, vizinho, caminho + [vizinho]))
                    
    print("\n[Falha] Não foi possível encontrar um caminho.")
    return None

if __name__ == "__main__":
    # Execução do cenário clássico do livro: de Arad a Bucareste
    caminho_solucao = busca_gulosa('Arad', 'Bucareste')
    
    if caminho_solucao:
        print("\nResultado do Caminho Escolhido:")
        print(" -> ".join(caminho_solucao))
