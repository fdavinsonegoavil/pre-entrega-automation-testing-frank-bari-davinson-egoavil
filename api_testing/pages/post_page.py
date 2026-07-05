import requests

class PostPage:
    def __init__(self):
        # URL base de la API para el TP
        self.base_url = "https://jsonplaceholder.typicode.com/posts"
        self.headers = {
            "Content-type": "application/json; charset=UTF-8"
        }

    def get_post(self, post_id):
        """Método GET: Obtiene un post específico por su ID"""
        url = f"{self.base_url}/{post_id}"
        response = requests.get(url, headers=self.headers)
        return response

    def create_post(self, title, body, user_id):
        """Método POST: Crea un nuevo recurso.
           Recibe los parámetros específicos respetando minúsculas y mayúsculas.
        """
        payload = {
            "title": title,
            "body": body,
            "userId": user_id  # Fíjate la 'I' mayúscula que pide la API
        }
        response = requests.post(self.base_url, json=payload, headers=self.headers)
        return response

    def update_post(self, post_id, title, body, user_id):
        """Método PUT: Actualiza un recurso existente por completo"""
        url = f"{self.base_url}/{post_id}"
        payload = {
            "id": post_id,
            "title": title,
            "body": body,
            "userId": user_id
        }
        response = requests.put(url, json=payload, headers=self.headers)
        return response

    def delete_post(self, post_id):
        """Método DELETE: Elimina un recurso específico por su ID"""
        url = f"{self.base_url}/{post_id}"
        response = requests.delete(url, headers=self.headers)
        return response