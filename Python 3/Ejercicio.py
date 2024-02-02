# Ejercicio 1
# se define la funcion f(x) = x^2 + 2
def f(x):
    return x**2 + 2

def area_under_f(n):

    area = 0
    width = (2 - 1) / n

    for i in range(n):
        height = f(1 + i * width)
        area += height * width
    return area
def f(x):
    return x**2 + 2

# Se define la funcion que computa el area bajo f(x) usando rectangulos
def area_under_f(n):
   
    area = 0   
    width = (2 - 1) / n

    for i in range(n):
        height = f(1 + i * width)       
        area += height * width

    return area