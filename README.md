# SauceDemo Automation Project

Este proyecto contiene la automatización de pruebas para la página SauceDemo utilizando Python, Selenium y Pytest, estructurado bajo el patrón de diseño Page Object Model (POM).

## Configuración del Entorno

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### 1. Navegar al directorio del proyecto
Abre tu terminal (Símbolo del sistema, PowerShell o Git Bash) y navega hasta la carpeta donde guardaste este proyecto. Sustituye la ruta del ejemplo por la ruta real donde ubicaste los archivos:

```bash
cd C:\ruta\a\tu\proyecto\saucedemo-automation
```

### 2. Crear el entorno virtual
Para evitar conflictos con otras bibliotecas en tu sistema, crea un entorno virtual aislado ejecutando:

```bash
python -m venv venv
```

### 3. Activar el entorno virtual
Dependiendo de tu sistema operativo, ejecuta el comando correspondiente para activarlo:

**En Windows (PowerShell/CMD):**
```bash
venv\Scripts\activate
```

**En macOS / Linux:**
```bash
source venv/bin/activate
```
*(Sabrás que está activado porque verás el prefijo `(venv)` al inicio de tu línea de comandos).*

### 4. Instalar las dependencias requeridas
Con el entorno virtual activado, instala las bibliotecas de automatización ejecutando:

```bash
pip install -r requirements.txt
```
### 5. Ejecutar las Pruebas

Una vez configurado el entorno y con el entorno virtual activo `(venv)`, puedes ejecutar las suites de prueba de manera independiente o completa.

#### Ejecutar las pruebas de la API (TP Final)
Para correr exclusivamente las pruebas de la API utilizando el archivo de configuración personalizado y aislar la ejecución:
```bash
pytest api_testing/ -c api_testing/pytest.ini