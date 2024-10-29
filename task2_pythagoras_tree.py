"""Завдання 2. Необхідно написати програму на Python, яка використовує рекурсію 
для створення фрактала “дерево Піфагора”. Програма має візуалізувати фрактал “дерево Піфагора”, 
і користувач повинен мати можливість вказати рівень рекурсії."""

import turtle

def set_turtle(tr):
    """Функція для встановлення параметрів відображення черепашки, зокрема розташування, швидкість та напрямок 
    малювання, колір лінії"""
    tr.hideturtle()
    tr.speed(15)
    tr.up
    tr.setpos(0,-200)
    tr.rt(-90)
    tr.down
    screen.colormode(255)
    tr.pencolor(155, 0,0)

def ptree(stp, scl, angl, lvl, tr):
    """Функція для створення дерева Піфагора. У якості параметрів приймає довжину кроку для руху вперед,
    масштаб, кут повороту, рівень рекурсії, та об'єкт класу turtle. Масштаб визначає, на скільки потрібно
    зменшити довжину кроку вперед на кожному наступному рівні рекурсії."""
    if lvl > 0:
        tr.forward(stp)
        tr.left(angl)
        ptree(stp*scl, scl, angl, lvl-1, tr)
        tr.left(-2*angl)
        ptree(stp*scl, scl, angl, lvl-1, tr)
        tr.left(angl)
        tr.forward(-stp)
        

if __name__ == "__main__":

    level =int(input("Вкажіть рівень рекурсії: "))   #встановлення рівня рекурсії

    if level:
        screen = turtle.Screen()
        rootwindow = screen.getcanvas().winfo_toplevel()            #додаткові налаштування,   
        rootwindow.call('wm', 'attributes', '.', '-topmost', '1')   #щоб черепашка не ховалась за IDE
        tree = turtle.Turtle()
        scale = 0.75
        step = 200
        angle = 45
        set_turtle(tree)
        ptree(step, scale, angle, level, tree)

    turtle.done()