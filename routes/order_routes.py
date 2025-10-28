from fastapi import APIRouter

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema.
    Todas as rotas de pedidos precisam da autenticação do usuário
    """
    return {"Mensagem": "Você acessou a rota de pedidos."}