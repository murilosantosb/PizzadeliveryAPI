from fastapi import APIRouter

auth_router = APIRouter(prefix="/auth", tags=["auth"])

@auth_router.get("/login")
async def user_login():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return [{"id": 1, "name": "Murilo"}]