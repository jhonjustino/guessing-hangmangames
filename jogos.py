import hangman
import guessing_game

print("**********************************")
print("*******Escolha o seu jogo!********")
print("**********************************")

print("(1) Forca (2) Adivinhação")

jogo = int(input("Qual o jogo você escolhe? "))

if (jogo == 1):
    print("Jogando Forca")
    hangman.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação")
    guessing_game.jogar()
else:
    print("Não existe jogo com esse número")