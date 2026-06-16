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

# Guia Teórico e Prático: Algoritmo de Busca Gulosa (Greedy Best-First Search)

Este documento foi desenvolvido com o objetivo de servir como material pedagógico de apoio para estudantes de Inteligência Artificial. Aqui, encontrará uma explicação detalhada sobre o funcionamento teórico da **Busca Gulosa** e uma análise linha por linha do código Python implementado para resolver o problema clássico do **Mapa da Roménia** (Russell & Norvig).

---

## 1. O que é a Busca Gulosa?

A **Busca Gulosa (Greedy Best-First Search)** é um algoritmo de busca informada (ou heurística). O termo "gulosa" (ou *greedy*) provém do comportamento intrínseco do algoritmo: tomar sempre a decisão que parece ser a melhor **naquele exato momento**, sem olhar para trás e sem medir as consequências a longo prazo.

### Como funciona a tomada de decisão?
Ao contrário da busca cega (como a Busca em Largura ou Profundidade), a Busca Gulosa utiliza uma **função avaliação $f(n)$** que depende exclusivamente de uma **função heurística $h(n)$**:

$$f(n) = h(n)$$

No cenário do mapa da Roménia, a heurística $h(n)$ representa a **distância em linha reta** de uma determinada cidade até ao objetivo final (**Bucareste**). O algoritmo assume erroneamente que, se a Cidade A está mais perto de Bucareste em linha reta do que a Cidade B, então o caminho através de A será obrigatoriamente melhor.



### A "Miopia" e Limitações do Algoritmo
* **Ignora o Passado:** O algoritmo desconsidera por completo o custo real da estrada já percorrida para alcançar o nó atual ($g(n)$).
* **Não é Ótimo:** Devido a esta "miopia", a Busca Gulosa escolhe frequentemente atalhos locais rápidos que resultam num trajeto total mais longo. No nosso mapa, ela escolhe ir por *Fagaras* (heurística 176) em vez de *Rimnicu Vilcea* (heurística 193), ignorando que as estradas de Fagaras são muito mais longas, resultando num caminho final pior do que o da Busca A*.
* **Controlo de Ciclos:** Se o algoritmo for implementado como uma busca em árvore pura (sem guardar os nós já visitados), ele pode ficar preso em *loops* infinitos caso encontre cidades com heurísticas enganadoras. A nossa implementação mitiga isto transformando-a numa busca em grafo (usando um conjunto de visitados).



   
