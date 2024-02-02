#Ejercicio2
# se define la funcion g(x) = x
def g(x):
    return x

# Se define la funcion que computa el areea entre f(x) y g(x) usando rectangulos
def area_between_f_and_g(n):
    area = 0
    width = (2 - 1) / n
    for i in range(n):
        height = f(1 + i * width) - g(1 + i * width)
        area += height * width
    return area