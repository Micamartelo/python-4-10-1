salario = float(input('Escreva seu salario...'))
if salario <= 1250:   
    novo = salario +  (salario * 10 /100)
else:
    novo = salario + (salario *15/100)
print('Seu antigo salario é R${:.2f} e voce passa a ganhar R${:.2f})'.format(salario,novo))
