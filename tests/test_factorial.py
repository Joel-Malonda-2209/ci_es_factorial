import pytest
from src.factorial import *


def test_factorial():
    assert calcular_factorial(1) == 1


def test_TypeError():
    with pytest.raises(TypeError):
        calcular_factorial("aaaa")


def test_valueError():
    with pytest.raises(ValueError):
        calcular_factorial(-1)


def test_factorial_de_cinc():
    assert calcular_factorial(5) == 120
