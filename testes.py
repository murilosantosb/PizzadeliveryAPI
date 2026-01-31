import requests

headers = {
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOjEsImV4cCI6MTc2MjgwODM1NX0.lfChwieYHCFBgnGL_l3qJ5p065dpU_3OvlqYTwyoP64"
}

requisicao = requests.get("http://127.0.0.1:8000/auth/refresh", headers=headers)