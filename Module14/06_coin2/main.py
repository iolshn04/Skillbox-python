# TODO здесь писать код
def circle(x, y, r):
    x1 = r
    y1 = r
    x2 = -r
    y2 = -r
    if x > 0 and x1 >= x or y > 0 and y1 >= y:
        print('Монетка где-то рядом')
    elif x < 0 and x2 <= x or y < 0 and y2 <= y:
        print('Монетка где-то рядом')
    else:
        print('Монетки в области нет')


print('Введите координаты монетки:')
X = float(input('X: '))
Y = float(input('Y: '))
R = int(input('Введите радиус: '))

circle(X, Y, R)

# зачтено
