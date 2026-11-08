from analizador import contar_frecuencias


def test_frecuencias_basico():
    resultado = contar_frecuencias("sol luna sol")
    assert resultado["sol"] == 2
    assert resultado["luna"] == 1


def test_frecuencias_vacio():
    resultado = contar_frecuencias("")
    assert resultado == {}


def test_frecuencias_mayusculas():
    resultado = contar_frecuencias("Sol sol SOL")
    assert resultado["sol"] == 3


def test_espacios_extra():
    resultado = contar_frecuencias("  sol   luna  sol  ")
    assert resultado == {"sol": 2, "luna": 1}
