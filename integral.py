import matplotlib.pyplot as plt
import numpy as np
import random
import scipy.integrate as spi

# Визначення функції та межі інтегрування
def f(x):
    return np.exp(-(x ** 2))

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = exp(-x^2) від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()


# Розрахунок інтеграла методом Монте-Карло
def is_inside(x, y):
    return y <= f(x)

def monte_carlo_simulation(a, b, num_experiments):
    Sm = 0

    for _ in range(num_experiments):
        # Генерація випадкових точок
        points = [(random.uniform(a, b), random.uniform(0, f(a))) for _ in range(15000)]

        # Відбір точок, що знаходяться під кривою
        inside_points = [point for point in points if is_inside(point[0], point[1])]

        # Кількість усіх точок та точок всередині
        N = len(points)
        M = len(inside_points)
        area = (M / N) * ((b-a) * f(a))  # Площа за методом Монте-Карло
        Sm+=area
    
    Sm /= num_experiments
    return Sm
    
Sm = monte_carlo_simulation(a, b, 100)
St, error = spi.quad(f, a, b)  # теоретична площа фігури

print(f"Інтеграл функції f(x)=exp(-x^2) від {a} до {b}")
print(f"Теоретичне значення інтеграла: {St}, інтеграл за методом Монте-Карло: {Sm}")
print(f"Різниця у площах, похибка розрахунку методом Монте-Карло: {round(((Sm - St) / St)*100, 5)}%")