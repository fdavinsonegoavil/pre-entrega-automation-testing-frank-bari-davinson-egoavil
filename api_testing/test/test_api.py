import pytest_check as check

def test_crear_nuevo_post(post_page, post_data):
    """Prueba el método POST usando datos dinámicos del fixture"""
    # Enviamos los datos desglosados del fixture 'post_data'
    response = post_page.create_post(
        title=post_data["title"],
        body=post_data["body"],
        user_id=post_data["userId"]
    )
    
    # Validaciones con pytest-check (no detienen el flujo si fallan)
    check.equal(response.status_code, 201, f"Código esperado 201, se obtuvo {response.status_code}")
    
    res_json = response.json()
    check.equal(res_json["title"], post_data["title"], "El título no coincide en la respuesta")
    check.equal(res_json["userId"], post_data["userId"], "El userId no coincide en la respuesta")

def test_obtener_post_existente(post_page):
    """Prueba el método GET buscando un ID específico"""
    id_a_buscar = 1
    response = post_page.get_post(id_a_buscar)
    
    check.equal(response.status_code, 200, f"Código esperado 200, se obtuvo {response.status_code}")
    
    res_json = response.json()
    check.equal(res_json["id"], id_a_buscar, "El ID retornado no es el solicitado")

def test_eliminar_post(post_page):
    """Prueba el método DELETE"""
    id_a_eliminar = 1
    response = post_page.delete_post(id_a_eliminar)
    
    check.equal(response.status_code, 200, f"Código esperado 200, se obtuvo {response.status_code}")