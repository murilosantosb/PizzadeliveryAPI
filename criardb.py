from database.models import Base, db

# cria todas as tabelas definidas nas classes que herdam de Base
Base.metadata.create_all(bind=db)

print("✅ Banco de dados criado com sucesso!")