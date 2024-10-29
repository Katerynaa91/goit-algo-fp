"""Завдання 6. Написати програму, яка використовує жадібний алгоритм та алгоритм динамічного програмування 
для розв’язання задачі вибору їжі з найбільшою сумарною калорійністю в межах обмеженого бюджету.
Розробити функцію greedy_algorithm жадібного алгоритму, яка вибирає страви, 
максимізуючи співвідношення калорій до вартості, не перевищуючи заданий бюджет.
Для реалізації алгоритму динамічного програмування створіть функцію dynamic_programming, 
яка обчислює оптимальний набір страв для максимізації калорійності при заданому бюджеті."""

def show_names(d, result):
	"""Допоміжна функція, яка шукає ключ словника (в даному випадку - назву їжі) через його значення"""
	for k in d:
		for i in range(len(result)):
			if result[i]==d[k]:
				result[i] = {k:result[i]}
	return result

def greedy_algorithm(itms, bgt, cls='calories', cst='cost'):
	"""Функція жадібного алгоритму. У якості параметрів приймає словник, де ключем є назва їжі, 
	значенням - інший словник, де ключі позначають категорії (калорійність та вартість), значення - 
	безпосередньо значення калорійності та вартості, відношення яких обчислюється у функції, та обмеження
	(сума, яку не має перевищувати сукупна ціна обраної їжі). Алгоритм полягає у наступному: 
	сортуємо вхідні дані від більшого до меншого (сортуємо по категорії калорійності, як категорії, 
	що предтавляє певну цінність), в циклі складаємо найбільші унікальні значення, поки вони не перевищують 
	обмеження. Повертаємо число сукупної калорійності обраних продуктів, та словник з переліком обраних позицій. 
	"""
	greedy_data = sorted(itms.values(), key=lambda x: x[cls], reverse=True)
	cost=0
	calories=0
	results = []
	for item in greedy_data:
		if cost + item[cst] <=bgt:
			results.append(item)
			cost+=item[cst]
			calories+=item[cls]
	results = show_names(itms, results)
	return calories, results

def dynamic_programming(itms, bgt, cls='calories', cst='cost'):
	"""Функція динамічного рограмування. Використовує матрицю для пошуку оптимальних значень цінності при
	встановлених обмеженнях, порівнюючи попередні та поточні значення. Функція Повертає значення 
	сукупної калорійності обраних продуктів, та словник з переліком обраних позицій """
	n = len(itms)
	dp = [[0 for _ in range(bgt+1)] for _ in range(n+1)]
	
	for i in range(n+1):
		for w in range(bgt+1):
			if i == 0 or w==0:
				dp[i][w]==0
			elif itms[i-1][cst]<=w:
				dp[i][w] = max(itms[i-1][cls] + dp[i-1][w - itms[i-1][cst]], dp[i-1][w])
			else:
				dp[i][w]=dp[i-1][w]
	
	w = bgt
	results = []
	for i in range(n, 0, -1):
		if dp[i][w]!=dp[i-1][w]:
			results.append(itms[i-1])
			w-=itms[i-1][cst]
	total_value = dp[n][bgt]
	return total_value, results

def dynamic_main(itms, bgt):
	"""Допоміжна функція для виведення результатів функції dynamic_programming()"""
	data = [itms[k] for k in itms]
	total, selected = dynamic_programming(data, bgt)
	selected = show_names(itms, selected)
	return total, selected


if __name__=="__main__":
	
	BLUE = '\033[34m'
	GREEN = '\033[32m'
	RESET = '\033[0m'

	items = {
			"pizza": {"cost": 50, "calories": 300},
			"hamburger": {"cost": 40, "calories": 250},
			"hot-dog": {"cost": 30, "calories": 200},
			"pepsi": {"cost": 10, "calories": 100},
			"cola": {"cost": 15, "calories": 220},
			"potato": {"cost": 25, "calories": 350}
	}

	budget = 250

	print(BLUE + 'DYNAMIC PROGRAMMING' + RESET)
	print(dynamic_main(items, budget))
	print(GREEN + 'GREEDY ALGORITHM' + RESET)
	print(greedy_algorithm(items, budget))




