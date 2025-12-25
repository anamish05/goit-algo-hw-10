import pulp

# Ініціалізація моделі
model = pulp.LpProblem("Maximize-Production", pulp.LpMaximize)

# Визначення змінних
lemonade = pulp.LpVariable('L', lowBound=0, cat='Integer')  # Кількість лимонаду
juice = pulp.LpVariable('J', lowBound=0, cat='Integer')  # Кількість соку

# Функція цілі (Максимізація виробництва)
model += lemonade + juice, "Lemonade_and_Juice"

# Додавання обмежень
model += 2 * lemonade + 1 * juice <= 100  # Обмеження для води
model += lemonade <= 50  # Обмеження для цукру
model += lemonade <= 30  # Обмеження для лимонного соку
model += 2 * juice <= 40  # Обмеження для цукру

# Розв'язання моделі
model.solve()

# Вивід результатів
print("Виробити лимонаду:", lemonade.varValue)
print("Виробити соку:", juice.varValue)

print(f"Всього продукції = {pulp.value(model.objective)}")
