import random

numero_secreto = round(random.random() * 100)
tentativas = 3

print(numero_secreto)

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
        print("Voce acertou!")
        print(numero_secreto)
        break    
    else:
        if (maior):
            print("Voce Errou! seu numero foi maior que o numero secreto.")
        elif (menor):
            print("Voce Errou! seu numero foi menor que o numero secreto.")

print("O numero secreto era ", numero_secreto)        
print("Fim Do Jogo!")
print("Obrigado por ter jogado!!!")
