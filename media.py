
#git status
titulo = "Media de dois valores"
print(f'{titulo:^30}')

x = float(input('Entre com o valor de x: '))
y = float(input('Entre com o valor de y: '))
z = float(input('Entre com o valor de z: '))
media = (x+y+z)/3
print("O valor de x é", x, "!")
print('O valor de y é', y)
print('A media dos valores é', round(media, 3))