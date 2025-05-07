print('01 navio com 04 posições')
print('02 navios com 03 posições')
print('03 navios com 02 posições')
print('04 navios com 01 posição.')

matriz = [['A' for _ in range(10)] for _ in range(10)]

x= 0

lin = int(input('Qual a linha deseja posicionar o navio (1 a 10)?'))

col = int(input('Qual a coluna inicial (1 a 10)?'))

if col > 7:
    print('Erro, a posição selecionada ultrapassa os limites do tabuleiro')
elif col-1 == 'A':
    print('não é possivel colocar o barco nessa posição')
elif col =='A':
    print('não é possivel colocar o barco nessa posição')
elif col+1 == 'A':
    print('não é possivel colocar o barco nessa posição')
elif col+2 == 'A':
    print('não é possivel colocar o barco nessa posição')
elif col+3 == 'A':
    print('não é possivel colocar o barco nessa posição')
elif col+4 == 'A':
    print('não pode colocar o barco nesta posição')
elif col+5 == 'A':
    print('não pode colocar o barco nesta posição')
elif col+6 == 'A':
    print
else:
    matriz[lin-1][col-1]="N"
    matriz[lin-1][col]="N"
    matriz[lin-1][col+1]="N"
    matriz[lin-1][col+2]="N"


    print(matriz[0])
    print(matriz[1])
    print(matriz[2])
    print(matriz[3])
    print(matriz[4])
    print(matriz[5])
    print(matriz[6])
    print(matriz[7])
    print(matriz[8])
    print(matriz[9])
    print(matriz[10])
