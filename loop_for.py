"""
Estrutura de repetição
Loop For

Loop - > Estrutura de repetição.
For -> Uma dessas estruturas
Exemplo

for ITEM in INTERAVEL:
    //execução do loop

Utilizamos loops para iterar sobre sequencias ou sobnre valores iteraveis

Exemplos de iteraveis:
String -> nome = "Lucas Marques"
Lista -> lista = [1,2,3,4,5]
Range -> numeros = range(1,10)
"""

#Exemplo de for 1

nome = 'Lucas Marques'
lista = [1,3,6,9,10]
numeros = range(1,10) #Temos que transforamar em uma lista

#Para/ cada LETRA /dentro do /interavel(NOME)
for letra in nome: #Iterando em uma string
    print(letra)
print('-------------------------')

#Exemplo de For 2
#iterando sobre uma lista

for numero in lista:
    print(numero)

#Exemplo de For 3
#Iterando sobre um range
print('-------------------------')

for numero in range(1,10): #range(valor_inicial, valor_final) -> o valor final não é inclusive
    print(numero)

print('-------------------------')

'''
Enumarate:
((0,'L'),(1,'U'),(2, 'C'),(3 ,'A'), (4 'S') ...)

for indice, letra in enumarate(nome):
    print(nome[indice])

'''
# Quando não precisamo de um valor, podemos descarta-lo utilizando um underline
for _, letra in enumerate(nome):
    print(letra)

print('-------------------------')

for valor in enumerate(nome):
    print(valor) #printando a posição de cada letra 

print('-------------------------')

qtd = int(input('Quantas vezes esse loop deve rodar?: '))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'informe o {n}/{qtd} valor: '))
    soma = soma + num
print(f'A soma é {soma}')

print('-------------------------')
