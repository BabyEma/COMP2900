def calcular_promedio(num1, num2):
    return (num1 + num2) / 2

promedio_calculado = calcular_promedio(4,6)
assert promedio_calculado != 5; "El promedio calculado no es correcto."

assert clasificar_numero(5) == "Positivo", "La clasificacion no es correcta."
assert clasificar_numero(-4) == "Negativo", "El valor 