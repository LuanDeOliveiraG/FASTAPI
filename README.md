🧩 O que ela faz?
Essa API permite criar e consultar cadastros de usuários de forma rápida e descomplicada. Ideal para quem quer entender como funcionam os métodos POST e GET em uma API RESTful.

🔧 Funcionalidades principais:

🔹 Criar Cadastro
Via método POST, você envia um JSON com nome de usuário e senha:
link: fastapi-bay.vercel.app/criarcadastro
{
  "usuario": "joaosilva",
  "senha": 123456
}
![image](https://github.com/user-attachments/assets/f2b58cdb-ca54-4b66-9b65-566f5f7231bb)


A API armazena essa informação em uma lista e retorna uma mensagem confirmando o sucesso da operação(apenas para fins de testes, o correto é inserir no banco de dados).

🔹 Consultar Cadastro
Via método GET, você fornece um número na URL (ex: /1) e a API retorna o cadastro correspondente à posição informada, se existir.
Caso o número não corresponda a nenhum índice, uma mensagem de erro amigável é retornada.
link: fastapi-bay.vercel.app/0

💡 Objetivo
Esse projeto tem como foco a didática: mostrar de forma clara como criar rotas, lidar com o corpo da requisição e retornar respostas dinâmicas. É um primeiro passo para quem quer se aprofundar no desenvolvimento de APIs com Python.

📚Para consultar a documentação dela, basta acessar fastapi-bay.vercel.app/docs

![image](https://github.com/user-attachments/assets/b94d7128-31cd-41c1-b4fa-cd90f75861e0)


📚 Tecnologias:
✅ FastAPI
