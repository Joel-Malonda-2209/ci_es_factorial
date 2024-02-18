"""mòdul càlcul factorial"""
def calcular_factorial(num):
    """
    funció per a calcular el factorial


    entrada: 
    - enter: num
    eixida:
    - enter: resultat de calcular el factorial
    """
    if num == 1:
        return 1
    if not isinstance(num,int):
        raise TypeError("Error, te que ser un número")
    if num < 0:
        raise ValueError("Error de número negatiu")
    return num * calcular_factorial(num - 1)
