selecoes = [
    'malasia',
    'china',
    'gabao',
    'malta'
]

selecao = input('Digite a seleção desejada: ')
find = False

for i in range(len(selecoes)):

    if selecao.upper() == selecoes[i].upper():
        find = True

if find:
    print('Achei')
else:
    print('Não achei')