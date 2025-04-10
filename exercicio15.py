numero = int(input('Digite o numero da tabuada: '))

for m in range(1, 11):
    print(f'{numero} x {m} = {numero * m}')


ciclos = 1

while ciclos <= 10:
    resultado = numero * ciclos
    print(f'{numero} x {ciclos} = {resultado}')

    ciclos += 1