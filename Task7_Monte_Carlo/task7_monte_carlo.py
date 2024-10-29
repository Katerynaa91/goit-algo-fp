"""Завдання 7. Написати програму, яка імітує велику кількість кидків кубиків, 
обчислює суми чисел, які випадають на кубиках, і визначає ймовірність кожної можливої суми.
Створити симуляцію, де два кубики кидаються велику кількість разів. 
Підрахувати, скільки разів сума чисел, які випали на обох кубиках (від 2 до 12), з’являється у процесі симуляції. 
Використовуючи ці дані, обчислити імовірність кожної суми. На основі проведених імітацій створити 
таблицю або графік, який відображає ймовірності кожної суми, виявлені за допомогою методу Монте-Карло.
Порівняти отримані за допомогою методу Монте-Карло результати з аналітичними розрахунками, наведеними в таблиці"""
import random
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
from plottable import Table, ColumnDefinition, cmap
from time import sleep


#Кидаємо 100 разів, рахуємо ймовірність. Так робимо 10 разів. Рахуємо середню ймовірність для 100 кидків в 10 сесіях.
def simulate(n, test_item=None):
    """Функція для генерації двох випадкових чисел від 1 до 6, що імітує кидання двох кубиків, n разів"""
    if test_item is None:
        test_item = [1,2,3,4,5,6]
    results = []
    for _ in range(n):
        x = np.random.choice(test_item, 2)
        results.append(sum(x))
    return sorted(results)

def probability(n):
    """Функція для підрахування ймовірності випадання кожної суми. Підраховуємо, скільки разів випала кожна сума
    при киданні n разів, знаходимо ймовірність випадіння, поділивши отримане значення на загальну кількість кидків.
    Функція повертає словник, де ключ - сума на двох кубиках, значення - обчислена ймовірність для кидків n разів"""
    res = {}
    vals = simulate(n)
    for val in vals:
        res[val]=1 if not res.get(val) else res[val]+1

    res = {k:v/n for k, v in res.items()}
    return res


def mean_probability(sessions, n):
    """Функція, яка повторює вище наведений експеримент ще певну кількість разів, для отримання більшої кількості
    експериментальних даних та перевірки точності результатів. Тобто, якщо результати попередньої функції і поточної
    функції не сильно відрізняються, можна зробити висновок, що n разів достатньо для визначення приблизної
    ймовірності і обрані об'єкти експерименту підлягають певній закономірності. Якщо результати відрізняються,
    значить, що або треба більша кількість імітацій, або даний об'єкт не має закономірності і має високий рівень
    випадковості"""

    temp = []
    for _ in range(sessions):
        prob = probability(n)
        temp.append(prob)
    
    means = {}

    for i in temp:
        for k, v in i.items():
            means[k]=v if not means.get(k) else means[k]+v
    
    means = {k: v/sessions for k, v in means.items()}

    return means, temp

def stats_table(data, title='Monte Carlo Cube Probability'):
    """Функція для виведення результатів обчислення за методом Монте-Карло у вигляді таблиці"""
    df = pd.DataFrame({'Number': [k for k in data.keys()], 'Probability %': [round(v*100, 3)for v in data.values()]})

    fig, ax = plt.subplots(figsize=(5, 5), label = title)
    ax.set_facecolor('#3d85c6')
    tab = Table(df)

    tab = Table(df,
        column_definitions=[ColumnDefinition(name="Probability %", 
        cmap=cmap.normed_cmap(df["Probability %"], cmap=plt.cm.Blues)),
        ColumnDefinition(name="Number", cmap=plt.cm.Blues),
        ColumnDefinition(name="index", cmap=plt.cm.Blues)])
    plt.show()

def stats_plot(func, n, rounds, mode=True):
    """Функція для виведення результатів обчислення за методом Монте-Карло у вигляді графіку"""
    fig, ax = plt.subplots(figsize=(8, 7), label = 'Monte Carlo Cube Digits Sum Probability')
    for i in rounds:
        p = func(n)
        ax.plot([x for x in p.keys()], [y*100 for y in p.values()], label = f'Experiment {i}')
        ax.spines[['right', 'top', 'left', 'bottom']].set(alpha=0.3)

    plt.xticks(range(1,13))
    plt.xlabel('Cube Digits')
    plt.ylabel('Probability, %')
    plt.grid(alpha=0.3)
    plt.legend(loc='upper right', fontsize='x-small', labelcolor='linecolor')
    plt.show()


if __name__=="__main__":
    n= 100
    times = 10
    test, prob = mean_probability(times, n)

    stats_table(test)
    stats_plot(probability, 100, range(1, 11))

    print(test)



