dv = int(input('Qual é a distancia ate o seu destino?'))
custo = (dv) * 0.50
custo2 = (dv) * 0.45

if dv <= 200: 
    print('Você vai pagar R${}'.format(custo))
else:
    print('Você vai pagar R${}'.format(custo2))