from calculos import inteiros
import math

numero = int(input('Digite um numero: '))

print(f'Fatorial de {numero} é {inteiros.fatorial(numero)}.')
print(f'O dobro de {numero} é {inteiros.dobro(numero)}.')
print(f'O triplo de {numero} é {inteiros.triplo(numero)}.')

print(f'A raiz quadrada de {numero} é {math.sqrt(numero)}')
