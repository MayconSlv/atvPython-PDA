# leia um valor interio entre 1 e 12, correspondente a este valor, deve ser apresentado como resposta o mês do valor por extenso, em inglês, com a primeria letra maiúscula


meses = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}


valor = int(input('Digite um valor'))

if valor > 0 and valor < 13:
    print(meses[valor])
else:
    print('Mês inválido')