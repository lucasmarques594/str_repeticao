#Exercicio 1
"1. Faça um programa que determine e mostre os cinco primeros multiplos de 3, considerando números maiores que 0."
print('--------------')

contador: int = 0
indice: int = 1

while contador < 5:
    if indice % 3 == 0:
        print(f'O numero {indice} é multiplo de 3.')
        contador = contador + 1
    indice = indice + 1

#Exercicio 2
'2. Faça um programa que utilize o comando while para mostra na tela uma contagem regressiva, iniciando em 10 e terminando 0. Mostre também uma mensagem "FIM!" após a contagem.'
print('--------------')

contador1: int = 10

while contador1 >= 0:
    print(contador1)
    contador1 = contador - 1
print('FIM!')

#Exercicio 3
'3. Faça um programa que declare um inteiro, inicialize-o com 0, incrimente-o de 1000 em 1000, imprimindo seu valor na tela, até que seu valor seja 100000(cem mil)'
print('--------------')

for n in range(0,100001, 1000):
    print(n)
