def analizar_sistema_con_alpha():
    from sympy import symbols, Eq, solve

    # Definir la variable simbólica alpha y las variables x1, x2, x3
    alfa = symbols('alpha')
    x1, x2, x3 = symbols('x1 x2 x3')

    # Definir las ecuaciones del sistema
    ecuaciones = [
        Eq(x1 - x2 + alfa * x3, -2),
        Eq(-x1 + 2 * x2 - alfa * x3, 3),
        Eq(alfa * x1 + x2 + x3, 2)
    ]

    # Resolver el sistema de ecuaciones
    soluciones = solve(ecuaciones, (x1, x2, x3, alfa), dict=True)
    valores_alfa = [s[alfa] for s in soluciones]

    # Imprimir los valores de alfa para los cuales el sistema tiene solución
    for valor in valores_alfa:
        if valor != alfa:
            print(f"Para α = {valor}, el sistema tiene solución.")
        else:
            print("Para valores de α distintos a los encontrados, el sistema no tiene solución.")

# Ejecutar la función
analizar_sistema_con_alpha()
