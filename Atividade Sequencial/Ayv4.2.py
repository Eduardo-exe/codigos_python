lata = int(input("informe a quatidade de lata de 350ml: "))
garrafa1 = int(input("informe a quantidade de garrafas de 600ml: "))
garrafa2 = int(input("informe a quantidade de garrafas de 2L: "))

x = (lata*350+garrafa1*600)/1000+(garrafa2*2)

print(f"A quantidade de litros comprada foi de: {x} ")