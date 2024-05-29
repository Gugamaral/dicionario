import os

pessoa = {

    'Nome': input('Informe seu nome: '),
    'CPF': input('Informe seu CPF: '),
    'RGg': input('Informe seu RG: '),
    'Data de Nascimento': input('Informe sua data de nascimento: '),
    'Gênero': input('Informe seu gênero: '),
    'e-mail': input('Informe seu e-mail: '),
    'Telefone': input('Informe seu telefone: '),
    'Tipo Aanguíneo': input('Informe seu tipo sanguíneo: '),
    'Profissão': input('Informe sua profissão: '),
    'Empresa': input('Informe sua empresa: ')

}
os.system('cls')
print(f'{'-'*30} DADOS DA PESSOA {'-'* 30} \n ')


for chave in pessoa:
    print(f'{chave}: {pessoa.get(chave)}')



