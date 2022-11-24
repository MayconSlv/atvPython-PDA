#o twitter é conhecido por limitar as postagens em 280 caracteres. Conferir se um texto vai caber em um novo tuíte é o desafio.
tweet = input('O que você está acontecendo?')

if len(tweet) > 280:
    print("Ultrapassou o limite de caracteres!")
else:
    print(tweet)

