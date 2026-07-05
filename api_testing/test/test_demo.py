import pytest_check as check

def test_verificacion_entorno():
    # Una prueba simple para comprobar que el CI funciona
    valor_esperado = True
    check.equal(valor_esperado, True, "El entorno de pruebas funciona correctamente")