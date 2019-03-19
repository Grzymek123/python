from matplotlib.pyplot import *
from numpy import *
from numpy.random import *

z = []
for i in range(56, 101):
    y = 2 * i * i + 2 * i + 2
    z.append(y)
print(z)


print('Insert your value here:')
try:
    x = int(input())
    silnia = 1;
    if x > 0:
        for i in range(1, x + 1):
            silnia = silnia * i
        print("silnia=", silnia)
    else:
        print("Nie można policzyć silni dla ujemnej wartości")
except ValueError:
    print("Wpisz liczbę!")


print('put the length of array: ')
m = int(input())
y=[]
for k in range(1, m+1):
    print('enter number: ')
    z = int(input())
    y.append(z)
print('Array : ')
print(y)
print('Min Value : ')
print(min(y))
indices = [i for i, m in enumerate(y) if m == min(y)]
print('Min Values Index: ')
print(indices)



print('enter value: ')
x = int(input())
x1=linspace(0, x, 200)
y=sin(x1)
plot(x1, y)
show()
