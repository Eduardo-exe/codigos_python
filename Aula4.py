texto = "Técnico em Desenvolvimento de sistemas"
print("******* titulo *******")
print("*"*10)
print(texto)

idade = int(input("Informe sua idade: "))
print("#"*idade)

#Manipulando textos(Strings)
print(f"O total de letras é", {len(texto)})

print(texto.upper())# upper() coloca todo o texto em maiusculo
print(texto.lower())# lower() coloca todo o texto em minusculo
print(texto.capitalize())# coloca a 1 letra em minusculo

print(texto.replace("sistemas","web"))# replcace troca um texto por outro

#trabalhando com fatiamaneto

print("fatiando a variavel texto")
print(texto[:3])#vai exibir todo o texto até a posição 2, no caso a posição 3 não conta
print(texto[3:])#vai exibir todo o texto a partir da posição 3
print(texto[3:10])#vai exibir todo o texto a partir que esta na posição 3 até 10