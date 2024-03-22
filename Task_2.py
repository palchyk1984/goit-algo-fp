import turtle
import math

def draw_tree(t, branch_length, level):
    if level == 0:
        return
    else:
        # Малюємо основний стовбур
        t.forward(branch_length)
        t.left(45)
        
        # Рекурсивно малюємо праву гілку
        draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
        
        t.right(90)
        # Рекурсивно малюємо ліву гілку
        draw_tree(t, branch_length * math.sqrt(2) / 2, level - 1)
        
        t.left(45)
        # Повертаємось до початкової позиції
        t.backward(branch_length)

def main():
    window = turtle.Screen()  # Створення вікна для малювання
    window.bgcolor("white")  # Встановлення кольору фону вікна
    
    t = turtle.Turtle()  # Створення черепашки для малювання
    t.left(90)  # Початкове поворот черепашки вгору
    t.color("green")  # Встановлення кольору черепашки
    
    t.speed('fastest')  # Встановлення максимальної швидкості малювання
    
    level = int(input("Введіть рівень рекурсії: "))  # Зчитування рівня рекурсії від користувача
    draw_tree(t, 100, level)  # Виклик функції для малювання дерева
    
    window.mainloop()  # Затримка закриття вікна

if __name__ == "__main__":
    main()
