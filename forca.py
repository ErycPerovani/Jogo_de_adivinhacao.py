def jogar():
    print("************************************")
    print("**** Bem vindo ao jogo da forca ****")  
    print("************************************")

    palavra_secreta = "Avocator"

    enforcou = False
    acertou = False

    while(not enforcou and not acertou):

        chute= input("Diga uma letra: ")
        chute= chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                print("encontrei a letra {} na posição {}".format(chute, index))
            index = index + 1
        print("jogando ...")

    print("Fim do Jogo!!")

if(__name__ == "__main__"):
    jogar()