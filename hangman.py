import random
def jogar():
    #A palavra secreta que o jogador irá adivinhar
    animals = ['gato','cachorro', 'cavalo', 'vaca', 'elefante', 'crocodilo', 'galinha']
    fruits = ['banana', 'uva', 'abacaxi', 'maçã', 'jabuticaba', 'melancia', 'morango']
    words = animals, fruits
    #Seleciona uma variável aleatória e depois dentro da variável seleciona a palavra aleatória dela
    secretWord = random.choice(random.choices(words, weights=map(len,words))[0])
    lettersGuessed = ""

    #O número de turnos antes do jogador perder
    failureCount = 0

    #Nível de dificuldade do jogo
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    print(secretWord)

    nivel = int(input("Defina o nível: "))
    #Define a quantidade de falhas que pode ter de acordo com o nível
    if(nivel == 1):
        failureCount = 20
    elif(nivel == 2):
        failureCount = 10
    elif(nivel == 3):
        failureCount = 5
    else:
        print("Não existe esse nível digitado, favor digitar os valores corretos.")
    #O loop vai ocorrer até o jogador errar todas as tentativas
    #Vai 'quebrar' o loop se o jogador acertar a palavra
    while failureCount > 0:
        #Perguntar a letra pro jogador.
        guessReal = input("Digite uma letra: ")
        #Ignora letra maiúscula e minuscula
        guess = guessReal.casefold()
        #Evita que a pessoa coloque mais de uma letra e acerte tudo direto
        if len(guessReal) > 1:
            print("Você deve digitar apenas uma letra")
            continue
        #Evita de digitar números, somente letra
        if guessReal.isnumeric():
            print("Você deve digitar apenas letras")
            continue

        if guess in secretWord:
            #Player acerta a letra
            print(f"Parabéns, você acertou a letra {guess} !!")
        else:
            #Se errar, irá diminuir a tentativa do jogador
            failureCount -= 1
            print(f"Errou, não existe a letra {guess} na palavra secreta, você tem {failureCount} tentativas restantes!!")

        #Mantém a letra que foi informada pelo jogador, salvo na variável letterGuessed
        lettersGuessed = lettersGuessed + guess
        wrongLetterCount = 0

        for letter in secretWord:
            if letter in lettersGuessed:
                print(f"{letter}", end="")
            else:
                print("_", end="")
                wrongLetterCount += 1
        print("")
        #Se não tiver letra errada, o jogador venceu
        if wrongLetterCount == 0:
            print(f"Parabéns, a palavra secreta era: {secretWord}. Você venceu!!")
            break

    else:
        print("Infelizmente você perdeu, tente novamente !!")

if(__name__ == "__main__"):
    jogar()
