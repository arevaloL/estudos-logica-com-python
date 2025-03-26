# Neste algoritmo, crie uma variável que armazene uma string e uma lista que armazena várias strings.

string = ''
lista = []

# Insira a resposta na variável a1 e crie um loop que solicite a inserção de novas strings até que a resposta seja 0.
while True:
    a1 = input("Deseja inserir uma nova string? Digite 1 para sim e 0 para não: ")
    if a1 == '1':
        string = input("Digite uma string: ")
        lista.append(string)
    elif a1 == '0':
        print("Você não deseja inserir uma nova string")
        break
    else:
        print("Entrada inválida. Por favor, digite 1 para sim ou 0 para não.")

# Imprima a lista
print("A lista contém: ", lista)
