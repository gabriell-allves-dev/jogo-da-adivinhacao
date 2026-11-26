import random

print('='*6 + 'JOGO DA ADIVINHAÇÃO' + '='*6)

num = random.randint(1,100)
print('Estou pensando em um número entre 1 e 100...')
print('Será que você consegue descobrir?')

palpite = int(input('Digite seu palpite: '))

if palpite < num:
    print('Quase lá')
    print('Tente um número maior')

elif palpite > num:
    print('Quase lá')
    print('Tente um número menor')

else:
    print(f'Número escolhido: {num}')
    print(f'Palpite escolhido: {palpite}')
    print('Parabéns você acertou!')