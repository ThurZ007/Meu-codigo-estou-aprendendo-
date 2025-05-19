import random
lista_de_palavras = ['gato', 'cachorro', 'galinha']
palavra_secreta = random.choice(lista_de_palavras)
palavra_digitada = ""
contador = 0
print("Dica: Nome de animais")


while True:
    letra = input("Digite uma letra para descobrir a palavra secreta: ")
    try:
        if len (letra) > 1:
            print("Digite somente uma palavra")
            contador += 1
            continue
        
        if letra in palavra_secreta:
            palavra_digitada += letra 
            print (letra)
            
            if sorted (palavra_digitada) == sorted (palavra_secreta):
                print("parabens vc acertou a palavra secreta, ")
                print (contador,
                "foi o tanto de chances que vc usou")
                break 
            continue
        
        else:
            print("*")
            contador += 1
            continue
        
    except:
        (palavra_secreta)
vai estudar
