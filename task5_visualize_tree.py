"""Завдання 5. Використовуючи код із завдання 4 для побудови бінарного дерева, 
необхідно створити програму на Python, яка візуалізує обходи дерева: у глибину та в ширину.
Вона повинна відображати кожен крок у вузлах з різними кольорами.
Кольори вузлів мають змінюватися від темних до світлих відтінків, залежно від послідовності обходу. 
Кожен вузол при його відвідуванні має отримувати унікальний колір, який візуально відображає порядок обходу.
Використати стек та чергу, НЕ рекурсію"""

import matplotlib.pyplot as plt
import networkx as nx
import heapq as hq
from task4_pyramid import add_edges, createHeap

def draw_tree(tree_root, func, cmap=plt.cm.Blues, title = 'Tree Traversal'):
    """Функція для вібображення графа. У якості параметрів приймає об'єкт класу Node (дерево), функцію обходу дерева
    (у глибину або в ширину) та додаткові необов'язкові параметри для зображення графа.
    Клас дерева надає атрибути, що визначають позиції та назви вузлів у графів.
    Кольори вузлів визначає послідовність, за якою вузли обходяться у процесі виконання функції обходу. 
    Світлі кольори відповідають початку обходу, темні кольори вказують на вузли, які обходяться останніми"""
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colordict = {func[i]: i for i in range(len(func))}
    color =[colordict[node[1]['label']] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5), label = title)
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=color, cmap=cmap)
    plt.show()
    

def bfs(node):
    """Функція для обходу графа (дерева) в ширину. У якості параметра функція приймає вузел класа дерева (Node).
    Обхід реалізується через додавання та видалення вузлів з черги. 
    Спочатку розглядаються ліві нащадки, потім - праві"""
    if node is None:
        return
    
    q = [node]
    visited = []
    while q:
        current = q.pop(0)
        visited.append(current.val)
        if current.left:
            q.append(current.left)
        if current.right:
            q.append(current.right)
    return visited

def dfs(node):
    """Функція для обходу графа (дерева) в глибину. У якості параметра функція приймає вузел класа дерева (Node).
    Обхід реалізується через стек. Спочатку розглядаються праві нащадки, потім - ліві"""
    if node is None:
        return
    visited = []
    stack = [node]
    
    while stack:
        current = stack.pop()
        visited+=[current.val]  
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
    return visited


if __name__=='__main__':

    vals = [5, 4, 65, 10, 11, 3, 8, 20, 15, 7]
    hq.heapify(vals)
    tr = createHeap(vals, 0)
    bf = bfs(tr)
    df = dfs(tr)

    draw_tree(tr, df, title = 'DFS Tree Traversal')
    draw_tree(tr, bf, cmap=plt.cm.Reds, title = 'BFS Tree Traversal')
  