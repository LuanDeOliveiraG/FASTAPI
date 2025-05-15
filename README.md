🧩 O que ela faz?
Essa API permite criar e consultar cadastros de usuários de forma rápida e descomplicada. Ideal para quem quer entender como funcionam os métodos POST e GET em uma API RESTful.

🔧 Funcionalidades principais:

🔹 Criar Cadastro
Via método POST, você envia um JSON com nome de usuário e senha:

{
  "usuario": "joaosilva",
  "senha": 123456
}

A API armazena essa informação em uma lista e retorna uma mensagem confirmando o sucesso da operação.

🔹 Consultar Cadastro
Via método GET, você fornece um número na URL (ex: /1) e a API retorna o cadastro correspondente à posição informada, se existir.
Caso o número não corresponda a nenhum índice, uma mensagem de erro amigável é retornada.

💡 Objetivo
Esse projeto tem como foco a didática: mostrar de forma clara como criar rotas, lidar com o corpo da requisição e retornar respostas dinâmicas. É um primeiro passo para quem quer se aprofundar no desenvolvimento de APIs com Python.

📚 Tecnologias:
✅ FastAPI
