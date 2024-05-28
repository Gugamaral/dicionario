dados = []

while True:
    dados.sort()
    novo_dado = input('Informe os dados na lista a seguir: ')

    if novo_dado != '':
        dados.append(novo_dado)
        continue
    else:
        break
pessoa = {
    
    'nome':'',
    'cpf':'',
    'rg':'',
    'data de Nascimento':'',
    'gênero':'',
    'e-mail':'',
    'telefone':'',
    'tipo sanguíneo':'',
    'profissão':'',
    'empresa':''
    }

pessoa['nome'] = input('Informe o nome: ')
pessoa['idade'] = int(input('Informe a idade: '))
pessoa['profissao'] = input('Informe a profissão: ')

for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')



