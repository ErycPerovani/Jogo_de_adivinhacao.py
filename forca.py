def jogar():
    print("************************************")
    print("**** Bem vindo ao jogo da forca ****")  
    print("************************************")

    palavra_secreta = "Bacana"
    letras_acertadas = ["_", "_", "_", "_", "_" ,"_"]
    letras_faltando = str(letras_acertadas.count("_"))

    enforcou = False
    acertou = False
    tentativas = 0

    while(not enforcou and not acertou):

        chute= input("Diga uma letra: ")
        chute= chute.strip()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_acertadas[index] = letra 
                index += 1
        else:
            tentativas += 1

        enforcou = tentativas == 6

        print(letras_acertadas)
        print('Ainda estao faltando {} letras'.format(letras_faltando))

    print("Fim do Jogo!!")

if(__name__ == "__main__"):
    jogar()