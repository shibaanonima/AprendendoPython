# numero = int(input('Digite a quantidade de clientes você quer cadastrar:'))
# cliente = [["jose", "maria", "joao"], [35, 40, 32], ["amarelo", "azul", "vermelho"]]

# print(cliente[0][1])
# print(cliente[1][1])
# print(cliente[2][1])

# vetor = [0 for i in range(numero)]

# for i in range(numero):

#     cliente.insert(i, input('Digite o nome do cliente:'))
# print(cliente)
# cliente.pop(1)
# print(cliente)

# numero = int(input('Digite a quantidade de clientes você quer cadastrar:'))
# vetor = [0 for i in range(numero)]
# for i in range(numero):
#     print(f'\n digite os dados da pessoa {i}')
#     nome = input('nome:')
#     idade = int(input('idade:'))
#     sexo = input('sexo:')
#     vetor[i] = {
#         "nome": nome,
#         "idade": idade,
#         "sexo": sexo
#     }
    # print(f'\n Lista de pessoas cadastradas:')
    # for pessoas in vetor:
    #     print(pessoas)
    # print(vetor[0]["sexo"])
b = 0
from random import randint
computador = randint(0,10)

a = int(input('Adivinhe um numero o numero da maquina: '))

print(f'a maquina escolheu: {computador}')

if a == computador:
    print('você acertou!!')
    
else:
    print('você errou!!')



