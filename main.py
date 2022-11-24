#Importar nosso arquivo Pessoa.py no diretório model
from  model.Pessoa import Pessoa

#Exemplo de uso
mauricio = Pessoa(1, 'mauricio')
print(mauricio)

#Quero mostrar só o nome   
print(mauricio.nome)