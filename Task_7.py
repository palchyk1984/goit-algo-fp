import random

def monte_carlo_simulation(num_trials):
    sums = [0] * 11  # Створюємо список для зберігання кількості випадань кожної суми (індекси від 2 до 12)
    
    for _ in range(num_trials):
        dice1 = random.randint(1, 6)  # Кидаємо перший кубик
        dice2 = random.randint(1, 6)  # Кидаємо другий кубик
        total = dice1 + dice2  # Обчислюємо суму
        
        # Збільшуємо лічильник відповідної суми
        sums[total - 2] += 1
    
    # Обчислюємо ймовірності кожної суми
    probabilities = [(count / num_trials) * 100 for count in sums]
    
    return probabilities

def print_probabilities_table():
    num_trials_list = [10, 100, 1000, 10000, 100000, 500000, 1000000]
    x_labels = list(range(2, 13))
    analytical_probabilities = [2.78, 5.55, 8.33, 11.11, 13.89, 16.67, 13.89, 11.11, 8.33, 5.56, 2.78]
    
    print("\nТаблиця імовірностей сум при киданні двох кубиків:")
    print("Кількість спроб\t" + "\t".join(["{:<13}".format(str(x)) for x in x_labels]))
    for num_trials in num_trials_list:
        row = ["{:<15}".format(f"{num_trials}")]
        probabilities = monte_carlo_simulation(num_trials)
        row.extend(["{:<15}".format(f"{prob:.2f}%") for prob in probabilities])
        print("".join(row))
    
    # Друкуємо теоретичні значення
    row = ["{:<15}".format("Теоретично")]
    row.extend(["{:<15}".format(f"{prob:.2f}%") for prob in analytical_probabilities])
    print("".join(row))

print_probabilities_table()
