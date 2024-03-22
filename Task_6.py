def greedy_algorithm(items, budget):
    # Створюємо список кортежів (назва, вартість, калорії)
    item_list = [(name, data["cost"], data["calories"]) for name, data in items.items()]
    # Сортуємо список за співвідношенням калорій до вартості у спадному порядку
    sorted_items = sorted(item_list, key=lambda x: x[2] / x[1], reverse=True)
    
    selected_items = []
    total_cost = 0
    total_calories = 0
    
    for name, cost, calories in sorted_items:
        if total_cost + cost <= budget:
            selected_items.append(name)
            total_cost += cost
            total_calories += calories
            
    return selected_items, total_calories

def dynamic_programming(items, budget):
    # Створюємо матрицю dp, де dp[i][j] буде максимальною кількістю калорій, 
    # яку можна отримати з вартості j з використанням перших i предметів
    dp = [[0] * (budget + 1) for _ in range(len(items) + 1)]
    
    for i, (name, data) in enumerate(items.items(), start=1):
        cost = data["cost"]
        calories = data["calories"]
        for j in range(1, budget + 1):
            if cost <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost] + calories)
            else:
                dp[i][j] = dp[i - 1][j]
    
    # Відновлюємо оптимальний набір предметів
    selected_items = []
    j = budget
    for i in range(len(items), 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(list(items.keys())[i - 1])
            j -= items[selected_items[-1]]["cost"]
    
    return selected_items, dp[-1][-1]

# Задана база даних про їжу
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

# Виклик жадібного алгоритму
selected_items_greedy, total_calories_greedy = greedy_algorithm(items, budget)
print("Жадібний алгоритм:")
print("Обрані страви:", selected_items_greedy)
print("Загальна кількість калорій:", total_calories_greedy)

# Виклик алгоритму динамічного програмування
selected_items_dp, total_calories_dp = dynamic_programming(items, budget)
print("\nАлгоритм динамічного програмування:")
print("Обрані страви:", selected_items_dp)
print("Загальна кількість калорій:", total_calories_dp)
