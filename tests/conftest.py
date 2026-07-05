import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    # 1. Configurar las opciones de Chrome
    options = Options()
    
    # Detectamos si estamos en GitHub Actions usando una variable de entorno automática de GitHub
    if os.environ.get('GITHUB_ACTIONS') == 'true':
        options.add_argument('--headless=new')  # Ejecuta Chrome sin ventana visual
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--window-size=1920,1080') # Simula una pantalla fija en la nube
    else:
        # Si estás en tu máquina local, mantienes tus preferencias visuales
        options.add_argument('--start-maximized')

    # 2. Inicializar el servicio y el Driver pasando las opciones
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    
    # Si estás en local, maximiza de forma clásica por las dudas
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        driver.maximize_window()
        
    yield driver
    
    # 3. Teardown (Cierre de sesión)
    driver.quit()