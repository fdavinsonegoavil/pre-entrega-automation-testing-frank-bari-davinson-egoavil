import pytest
from api_testing.pages.post_page import PostPage

@pytest.fixture(scope="class")
def post_page():
    """Fixture que inicializa la clase de servicio de la API"""
    return PostPage()

@pytest.fixture
def post_data():
    """Fixture que retorna los datos de prueba dinámicos para el POST"""
    return {
        "title": "Entrega Final QA Automation",
        "body": "Estructura del framework de APIs con Pytest",
        "userId": 12
    }