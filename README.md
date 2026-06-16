# Busca Gulosa - Problema do Mapa da Roménia (Russell & Norvig)

Este repositório contém uma implementação didática em Python do algoritmo de **Busca Gulosa (Greedy Best-First Search)**, utilizando o cenário clássico de navegação do mapa da Roménia. O exemplo e os dados foram extraídos do livro oficial *Inteligência Artificial: Uma Abordagem Moderna* de Stuart Russell e Peter Norvig.

## 📌 Contexto do Problema

O objetivo do algoritmo é encontrar um caminho num grafo partindo de uma cidade inicial (**Arad**) até à cidade de destino (**Bucareste**). 

A Busca Gulosa tenta minimizar o custo estimado para o objetivo avaliando os nós exclusivamente através da função heurística:
$$f(n) = h(n)$$

Onde $h(n)$ representa a **distância em linha reta** de uma determinada cidade até Bucareste.

### Tabela de Heurísticas $h(n)$ utilizadas:

| Cidade | $h(n)$ | Cidade | $h(n)$ |
| :--- | :---: | :--- | :---: |
| **Arad** | 366 | **Mehadia** | 241 |
| **Bucareste** | 0 | **Neamt** | 234 |
| **Craiova** | 160 | **Oradea** | 380 |
| **Drobeta** | 242 | **Pitesti** | 100 |
| **Eforie** | 161 | **Rimnicu Vilcea** | 193 |
| **Fagaras** | 176 | **Sibiu** | 253 |
| **Giurgiu** | 77 | **Timisoara** | 329 |
| **Hirsova** | 151 | **Urziceni** | 80 |
| **Iasi** | 226 | **Vaslui** | 199 |
| **Lugoj** | 244 | **Zerind** | 374 |

## 🚀 Como Executar o Projeto

### Pré-requisitos
Apenas necessita do **Python 3.x** instalado na sua máquina (não são necessárias bibliotecas externas, pois o algoritmo utiliza o módulo nativo `heapq`).

### Passos
1. Clone este repositório para a sua máquina local:
   ```bash
   git clone [https://github.com/SEU-UTILIZADOR/busca-gulosa-romenia.git](https://github.com/SEU-UTILIZADOR/busca-gulosa-romenia.git)
