from api import app
from fastapi.params import Body

cadastros = []

@app.get("/{numero}")
def home(numero: int):
    """retorna as informações"""
    if numero in range(len(cadastros)):
        return {'cadastro': f'{cadastros[numero]}'}
    else:
        return {'retorno' : "Id não Cadastrado"}



@app.post('/criarcadastro')
def criarcadastro(usuario:str = Body(...), senha:int = Body(...)):
    """Cadastro de usuario via post. {"usuario": "str","senha": numero inteiro}"""
    user = usuario
    senha_ = senha
    cadastros.append([user, senha_])
    return {'Usuário':f'{user}', "valor": f'{senha_}', 'Status': "criado com sucesso!"}
