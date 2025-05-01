import time

bd_filmes = []

def cadastra_filmes(bd, titulo, ano):
   filme = [titulo, ano]
   bd.append(filme)
   return bd

def lista_filmes(bd):
    for i in range(len(bd)):
        print(f'{i+1} | {bd[i][1]} | {bd[i][0]}')

def altera_filme(bd, indicie, titulo, ano):
    bd[indice][0] = titulo
    bd[indice][1] = ano
    return bd

while True:
    print('1 - Cadastrasr filme')
    print('2 - Listar filmes')
    print('3 - Alterar filme')
    op = int(input('Digite sua opção: '))

    if op == 1:
        
        bd_filmes = cadastra_filmes(bd=bd_filmes,
                        titulo=titulo,
                        ano=ano
                        )

        print('filme cadastrado')
    elif op == 2:
        lista_filmes(bd_filmes)
        print('filmes listados')
    elif op == 3:
        altera_filme()
        i = int('Qual filme deseja alterar? ')
        print('filme alterado')
    else:
        print(f"opção {op} invalida")

    time.sleep(3)