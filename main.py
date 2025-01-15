def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b 

def get_operation_choice(operations):
    while True:
        print("\nОберіть операцію:")
        for key, (name, _) in operations.items():
            print(f"{key}. {name}")

        choice = input("Введіть номер операції (1/2/3/4): ")
        if choice in operations:
            return choice
        else:
            print("Невірний вибір. Спробуйте ще раз.")

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Помилка: введіть коректне число!")

def calculator():
    operations = {
        "1": ("Додавання", add),
        "2": ("Віднімання", subtract),
        "3": ("Множення", multiply),
        "4": ("Ділення", divide)
    }

    while True:
        choice = get_operation_choice(operations)
        num1 = get_number("Введіть перше число: ")
        num2 = get_number("Введіть друге число: ")

        # Якщо хоча б одне число 0, повідомляємо про помилку
        if num1 == 0 or num2 == 0:
            print("Помилка: введене число 0. Не можна використовувати ділення на нуль!")
            continue  # Просимо користувача ввести числа знову

        _, operation = operations[choice]
        result = operation(num1, num2)

        print(f"Результат: {result}\n")
        repeat = input("Хочете виконати ще одну операцію? (так/ні): ").strip().lower()
        if repeat != "так":
            print("Дякуємо за використання калькулятора! До побачення!")
            break

calculator()