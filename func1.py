def hello(nome, Idade):
    print(f"Olá {nome}!")
    if (int(Idade) > 16):
        print("Você pode votar!")
    else:
        print("Você ainda não pode votar!")
hello("Isaac", 17)

hello("Peres", "14")