"""Завдання 4. Візуалізація піраміди
Наступний код виконує побудову бінарних дерев. Виконайте аналіз коду, щоб зрозуміти, як він працює.
Використовуючи як базу цей код, побудуйте функцію, що буде візуалізувати бінарну купу.
Примітка. Суть завдання полягає у створенні дерева із купи.

"""
import uuid

import networkx as nx
import matplotlib.pyplot as plt
import heapq as hq


class Node:
	"""Клас для реалізації дерева. Клас має атрибути, що позначають лівого та правого нащадка, 
	значення (ім'я) вузла, колір вузла (встановлений за замовчуванням, при бажанні можна змінити), 
	унікальний ідентифікатор вузла (далі використовуватиметься для побудові графа з дерева)"""

	def __init__(self, key, color="skyblue"):
		self.left = None
		self.right = None
		self.val = key
		self.color = color # Додатковий аргумент для зберігання кольору вузла
		self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
	"""Функція для створення графа з дерева. Функція має наступні параметри:
	graph - для передавання об'єкта класу nx.Graph (в даному випадку diGraph, оскільки граф орієнтований),
	node - для передавання вузлів класу дерева,
	pos - параметр для позиціонування вершин графа, представлений словником, де ключем є ідентифікатор вузла, 
	значенням - його координати на вікні візуалізцації,
	x, y - координати положення вузла (вершини),
	layer - рівень, на якому розташовуються вузли дерева на графі.
	Функція повертає об'єкт граф. Кроки, які виконуються у функції:
	- додається вузел у якості вершини графа; ідентифікатор вузла передається як параметр для
	додавання вершин графа, далі в коді саме ідентифікатор використовуватиметься для взаємодії класу дерева та графу; 
	також передається значення вузла, його використовуємо тільки для представлення вузла на графі при візуалізації.
	- якщо вузел має лівого нащадка, додається ребро, що з'єднує батьківський вузел та лівого нащадка;
	- якщо вузел має правого нащадка, додається ребро, що з'єднує батьківський вузел та правого нащадка;
	- положення лівого нащадка визначається як різниця між координатою х (починаючи з 0 для кореневого вузла) та 
	0.5 у ступені, що відповідає рівню дерева. Для кожного наступного рівня х приймає значення, 
	отримане для положення нащадка попереднього рівня, тобто батьківського вузла (наприклад, для рівня 1: left = 0 - 0.5**1 = -0.5; 
	для рівня 2: left = -0.5 - 0.5**2 = -0.75)
	- положення правого нащадка визначається як сума координати х (починаючи з 0 для кореневого вузла) та 
	0.5 у ступені, що відповідає рівню дерева. Для кожного наступного рівня х приймає значення, 
	отримане для положення батьківського вузла (наприклад, для рівня 1: right = 0 + 0.5**1 = 0.5)
	- координата у зменшується на 1 з кожним наступним рівнем та представляє ієрархічну структуру дерева;
	- повний обхід дерева та додавання усіх вузлів у якості вершин та ребер графа (зокрема, встановлення їх
	положення) досягається через рекурсивні виклики функції для лівого та правого піддерева. Саме через рекурсію 
	ми зменшуємо значення положення по Y та динамічно змінюємо значення X в залежності від X на попередньому кроці. 
	"""
	if node is not None:
		graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
		if node.left:
			graph.add_edge(node.id, node.left.id)
			l = x - 1 / 2 ** layer
			pos[node.left.id] = (l, y - 1)
			l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
		if node.right:
			graph.add_edge(node.id, node.right.id)
			r = x + 1 / 2 ** layer
			pos[node.right.id] = (r, y - 1)
			r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
	return graph


def draw_tree(tree_root):
	"""Функція для візуалізації дерева у вигляді графу за допомогою бібліотеки networkx.
	У якості параметра приймає об'єкт класа, що представляє дерево. Повертає зображення графа.
	Для визначення положення дерева на візуалізації, використовується функція add_edges, представлена вище.
	Також визначаються кольори графа та значення вершин, які відображатимуться."""
	tree = nx.DiGraph()
	pos = {tree_root.id: (0, 0)}
	tree = add_edges(tree, tree_root, pos)

	colors = [node[1]['color'] for node in tree.nodes(data=True)]
	labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

	plt.figure(figsize=(8, 5))
	nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
	plt.show()


def createHeap(arr, index):
	"""Функція для створення дерева з МіnHeap (мінімальна Купа). Перетворює елементи вхідного масиву на значення 
	об'єктів класу Купи. В даному випадку створюється мінімальна Купа, 
	де значення батьківських вузлів менше за значення візлів нащадків."""
	node = None
	if index < len(arr):
		if arr[index] == None:
			return
		node = Node(arr[index])
		node.left = createHeap(arr, 2*index+1)
		node.right = createHeap(arr, 2*index+2)
	return node


if __name__=="__main__":

	vals = [5, 4, 65, 10, 11, 3, 8, 20, 15, 7]
	hq.heapify(vals)
	tree = createHeap(vals, 0)
	draw_tree(tree)