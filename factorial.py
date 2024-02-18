def calcular_factorial(num):
    if num == 1:
        return 1
    
    if not isinstance(num,int):
        raise TypeError("Error, te que ser un número")

    if num < 0:
        raise ValueError("Error de número negatiu")

    else:
        return num * calcular_factorial(num - 1)