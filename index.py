import os
lista_de_compras = []
while True:
    resposta = input("Você quer (A)dicionar, (R)emover, (L)istar, (S)air ou (C)limpar terminal? ").strip().lower()
    
    if len(resposta) > 1:
        print("So uma caractere")
    
    elif resposta == "a":
        produto = (input("Digite seu produto: "))
        lista_de_compras.append(produto)
    
    elif resposta== "r":
        indice = input("Qual o numero do item que deseja? ")
        num_de_variavel = int(indice)
        del lista_de_compras[num_de_variavel]
    
    elif resposta == "l":
        for nome in enumerate(lista_de_compras):
            print(nome)
    
    elif resposta == "s":
        break
    
    elif resposta == "c":
        os.system('cls')

lista_de_compras_enumerada = enumerate(lista_de_compras)
print("Finalizando lista")
