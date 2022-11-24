# para doar sangue, é necessário ter:
# entre 16 e 69 anos
# pesar mais de 50kg
# estar descansado e ter dormido pelo menos 06hrs nas ultimas 24hrs

idade = int(input('Qual a sua idade?'))

if idade >= 16 and idade <= 69:
    peso = int(input('Quantos quilos você tem?'))
    if peso > 50:
        descansado = int(input('Quantas horas você dormiu na ultima noite?'))
        if descansado > 6:
            print('Você está liberado para doar sangue! SZ')
    else:
        print('Você não tem o peso necessário para doar sangue')
else:
    print('Você não tem a idade necessária para doar sangue.')