# Ejercicio 3
import random

# Se define la funcion que genera tres numeros distintos que sumen n
def generate_three_numbers(n):
    numbers = []
    while len(numbers) < 3:
        number = random.randint(1, n - 1)
        if number not in numbers and sum(numbers) + number <= n:
            numbers.append(number)
    return numbers