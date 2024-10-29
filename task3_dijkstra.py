"""Завдання 3. Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
використовуючи бінарну купу. Завдання включає створення графа, 
використання піраміди для оптимізації вибору вершин та обчислення 
найкоротших шляхів від початкової вершини до всіх інших."""

import networkx as nx
import heapq as hp
import matplotlib.pyplot as plt


def shortest_path(graph: nx.Graph, start: str, end: str = None):
    """Функція для знаходження найкоротшого шляху у графі. Має обов'язкові параметри об'єкту класа networkx graph
    та початкової вершини, та необов'язковий параметр - кінцева вершина. Якщо аргумент кінцевої вершини 
    не переданий, виводяться найкоротші відстані від початкової вершини до всіх інших вершин графа. Алгоритм
    функції використовує купу з модуля heapq. 
    Якщо окрема кінцева вершина не передана, функція повертає словник, де ключем є вершина, до якої визначається відстань
    від стартової вершини, значенням - відстань.
    Якщо визначена певна кінцева вершина, функція повертає кортеж, де першим елементом є відстань, другим - список
    вершин, через які проходить найкоротший шлях від стартової до кінуевої вершини."""
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]
    predecessors = {}

    while pq:
        path, current = hp.heappop(pq)
        if path > distances[current]:
            continue
        if end is not None:
            if current == end:
                break

        for neighbor, w in graph[current].items():
            new_path = path + w['weight']
            if new_path < distances[neighbor]:
                distances[neighbor] = new_path
                hp.heappush(pq, (new_path, neighbor))
                predecessors[neighbor] = current
    
    if end:
        p = []
        n = end
        while n != start:
            p.append(n)
            n = predecessors[n]
        p.append(start)
        p.reverse()

    return (distances[end], p) if end is not None else distances


#список ребер та їх ваги
e = [('O', 'S', 8), ('S', 'M', 1), ('M', 'I', 7), ('M', 'P', 1), ('P', 'I', 3), ('I', 'C', 3), ('C', 'B', 9), 
     ('B', 'K', 9), ('K', 'A', 4), ('K', 'T', 4), ('A', 'E', 4), ('E', 'H', 8), ('A', 'I', 3), ('A', 'F', 8),
     ('F', 'G', 5), ('G', 'R', 2), ('R', 'L', 6), ('A', 'C', 7), ('I', 'Q', 5), ('C', 'Q', 4), ('Q', 'T', 1),
    ('T', 'J', 4), ('T', 'S', 3), ('E', 'G', 4), ('P', 'R', 6)]

#список вершин
N = ['O', 'S', 'M', 'I', 
     'P', 'C', 'B', 'K', 
     'A', 'T', 'E', 'H', 
     'F', 'G', 'R', 'L', 
     'Q', 'J', ]

#створення графу, додавання вершин та ребер
G = nx.Graph()
G.add_nodes_from(N)
G.add_weighted_edges_from(e)

pos = {}

#координати для відображення вершин при візуалізації графа
p = [(1,8), (1.6,7), (3.5, 3.5), (1, 3), 
     (5.5, 3.5), (4.5,1.5), (2.9, 2.5), (2.4, 3),
     (3,4), (2,1), (3,7), (3, 8),
     (5,5), (6,5), (7, 5), (8, 5),
     (2.6, 1.5), (1, 1)]

for n, x in zip(G.nodes(data=True), p):
    n[1]['pos'] = x
    pos[n[0]] = x

edge_labels = {(u,v): d['weight'] for u,v,d in G.edges(data=True)} #додавання ваги ребер для візуалізації
nx.draw(G, pos=pos, with_labels=True, width=0.5)
nx.draw_networkx_edge_labels(G, pos=pos, edge_labels=edge_labels, label_pos=0.5)
plt.title('Dijkstra Algorithm')
plt.show()

#Example: Find shortest path from start point 'R' to end point 'T'
print(shortest_path(G, 'R', 'T')) # distance to the destination point
print(shortest_path(G, 'R'))      # no end point given. distances to all other vertices will be displayed
