#Importa nosso arquivo Pessoa.py no diretório model
from model.Pessoa import Pessoa
from database.Database import Database
from dao.PessoaDAO import PessoaDAO

#Exemplo de uso
mauricio = Pessoa(1, "Henrique Poyatos")
print(mauricio)

#Quero mostrar só o nome
print(mauricio.nome)

print("DAQUI PRA FRENTE É ACESSO AO BANCO...")

#Chama o objeto de banco de dados
db = Database()

#Instancia o objeto
pessoaDAO = PessoaDAO(db.conexao, db.cursor)

#Quero carregar uma lista com o que veio do banco de dados
pessoas = pessoaDAO.getAll(orderBy=True)
for pessoa in pessoas:
  print(pessoa)


#CRiar um objeto com qualquer ator/atriz/diretor/diretora

novo = Pessoa(0, 'Denzel Washington')

#Olha que simples

novo = pessoaDAO.save(novo)

#Consulta o banco de novo..
pessoas = pessoasDAO.getall(orderBy=True)
for pessoa in pessoas:
  print(pessoa)
  