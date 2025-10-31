from fastapi import APIRouter, Depends, HTTPException
from database.models import Usuario
from dependencies import take_session
from utils.security import bcrypt_context
# Types
from schemas.shemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session
from utils.security import ALGORITHM, ACCESS_TOKEN_EXPIRE, SECRET_KEY


from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone

auth_router = APIRouter(prefix="/auth", tags=["auth"])


def criar_token(id_usuario):
    data_expiracao = datetime.now(timezone.utc) + timedelta(days=ACCESS_TOKEN_EXPIRE)
    dic_info = {"sub": id_usuario, "exp": data_expiracao}
    jwt_codificado = jwt.encode(dic_info, SECRET_KEY, ALGORITHM)
    
    return jwt_codificado

def autenticar_usuario(email, senha, session: Session):
    usuario = session.query(Usuario).filter(Usuario.email==email).first()
    
    if not usuario:
        return False
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False

    return usuario

@auth_router.get("/")
async def home():
    """
    Essa é a rota padrão de autenticação do nosso sistema
    """
    return [{"id": 1, "name": "Murilo"}]


@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session: Session = Depends(take_session)):
    
    usuario = session.query(Usuario).filter(Usuario.email==usuario_schema.email).first()
    
    if usuario:
        raise HTTPException(status_code=400, detail="E-mail do usuário já cadastrado.")
    
    senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
    
    novo_usuario = Usuario(
        nome=usuario_schema.nome,
        email=usuario_schema.email,
        senha=senha_criptografada,
        ativo=usuario_schema.ativo,
        admin=usuario_schema.admin
    )
    
    session.add(novo_usuario)
    session.commit()
    
    return {"message":f"Usuário criado com sucesso. {novo_usuario.email}"}
    

@auth_router.post("/login")
async def login(login_schema: LoginSchema, session: Session = Depends(take_session)):
    
    usuario = autenticar_usuario(login_schema.email, login_schema.senha, session)
    
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado ou credenciais inválidas.")
    else:
        access_token = criar_token(usuario.id)
        return {
            "access_token": access_token,
            "token_type": "Bearer"
        }
       