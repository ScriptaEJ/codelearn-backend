from app.exceptions.exceptions import CategoriaSemNomeException, CategoriaExistenteException
from app.models.categoria_model import Categoria

def criar_categoria_service(data, db):
    nome = data.nome
    nome_formatado = nome.strip()

    categoria_existe = db.query(Categoria).filter(Categoria.nome == nome_formatado).first()

    if categoria_existe:
        raise CategoriaExistenteException()

    if not nome_formatado:
        raise CategoriaSemNomeException()


    nova_categoria = Categoria(
        nome=nome_formatado
    )

    db.add(nova_categoria)
    db.commit()