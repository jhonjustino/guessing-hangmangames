import random

def jogar():
    print("**********************************")
    print("Bem-vindos ao jogo de Adivinhação!")
    print("**********************************")

    numero_secreto = random.randrange(1,101)
    failureCount = 0
    pontos = 1000
    
    #Nível de dificuldade do jogo
    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")
    
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
    
    for rodada in range(1, failureCount + 1):
        print("Tentativa {} de {}".format(rodada, failureCount))

        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou " , chute_str)
        try:
            chute = int(chute_str)
        except ValueError:
            print("***Digite somente números***")
            continue

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        correto = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto

        if(correto):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            elif(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
