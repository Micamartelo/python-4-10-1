print('Analisador de um triangulo!')
t1 = float(input('Comprimento da primeira reta:'))
t2 = float(input('Comprimento da segunda reta:'))
t3 = float(input('Comprimento da terceira reta:'))
if t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2:
    print('Os segmentos pode formar um triangulo!')
else:
    print('Os segmentos não podem formar um triangulo :<')