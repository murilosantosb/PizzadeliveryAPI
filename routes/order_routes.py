from fastapi import APIRouter, Depends, HTTPException
from schemas.shemas import PedidoSchema
from sqlalchemy.orm import Session
from dependencies import take_session
from database.models import Usuario, Pedido

order_router = APIRouter(prefix="/orders", tags=["orders"])

@order_router.get("/")
async def pedidos():
    """
    Essa é a rota padrão de pedidos do nosso sistema.
    Todas as rotas de pedidos precisam da autenticação do usuário
    """
    return {"Mensagem": "Você acessou a rota de pedidos."}

@order_router.post("/pedido")
async def criar_pedido(pedido_schema: PedidoSchema, session: Session = Depends(take_session)):
   novo_pedido = Pedido(id_usuario=pedido_schema.id_usuario)
   session.add(novo_pedido)
   session.commit()
   return {"message": "Pedido criado com sucesso."}