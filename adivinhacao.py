import random

def jogar_adv(): 

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101)
    tentativas = 0
    pontos = 1000

    print(numero_secreto)

    print("[1] FACIL  [2] MÉDIO  [3] DIFICIL ")
    nivel = int(input("Qual dificuldade voce deseja? "))

    if(nivel == 1):
        tentativas = 12
    elif(nivel == 2):
        tentativas = 8
    else:
        tentativas = 5

    for rodada in range (1, tentativas + 1):
        print("tentativa {} de {}".format (rodada, tentativas))
        chute_str = input("Digite um numero entre 1 e 100: ")
        print ("Você Digitou ", chute_str)
        chute = int(chute_str)

        if( chute < 1 or chute > 100 ):
            print("Por favor, Digite um Numero de 1 a 100!")
            continue

        acertou = numero_secreto == chute
        menor = chute < numero_secreto
        maior = chute > numero_secreto

        if(acertou):
            pontos_perdidos = abs(pontos - chute)
            pontos = pontos - pontos_perdidos
            print("Voce acertou e fez {} pontos!".format(pontos))
            break    
        else:
            if (maior):
                print("Voce Errou! seu numero foi maior que o numero secreto.")
            elif (menor):
                print("Voce Errou! seu numero foi menor que o numero secreto.")
            
    print("Fim Do Jogo!")
    print("Obrigado por ter jogado!!!")
