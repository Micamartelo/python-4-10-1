ve = int(input('Qual é a velocidade do carro?'))
n1 = (ve-80) * 7
if ve >= 80:
    print('Você foi mutado!')
    print('A sua muta vai ser de {}'.format(n1))
else:
    print('Boa viagem!')
