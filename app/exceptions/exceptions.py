class CategoriaSemNomeException(Exception):
    def __init__(self, message='Categoria deve ter um nome.'):
        self.message = message
        super().__init__(message)

class CategoriaExistenteException(Exception):
    def __init__(self, message='Categoria com esse nome já existe.'):
        self.message = message
        super().__init__(message)
