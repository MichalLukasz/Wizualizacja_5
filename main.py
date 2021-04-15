import numpy as np

print('Zadanie 1')
a = np.array([4, 6, 5])
b = np.array([2, 4, 3])

print(a)
print(b)
print(a * b)

print('Zadanie 2')
c = np.arange(5 + 9 * 2, 5, -2).reshape(3, 3)
d = np.arange(60 - 16 * 5, 60, 5).reshape(4, 4)
print('Macierze:\n', c)
print(d)
print('Minima kolumn i rzędów:\n', c.min(axis=0))
print(c.min(axis=1))
print(d.min(axis=0))
print(d.min(axis=1))

print('Zadanie 3')
print(np.dot(a, b))

print('Zadanie 4')
a = np.array([2, 3, 6])
b = np.array([4.3, 5.5, 3.4])
# print(a.dtype, b.dtype)
print(np.dot(a, b))

print('Zadanie 5')
x = np.arange(6, 6 + 6 * 5, 5).reshape(2, 3)
print('Macierz:\n', x)
a = (np.sin(x))
print('Sinus:\n', a)

print('Zadanie 6')
x = np.arange(2.5, 6 * 3.2, 3.2).reshape(2, 3)
print('Macierz:\n', x)
b = (np.cos(x))
print('Cosinus:\n', b)

print('Zadanie 7')
print(np.add(a, b))

print('Zadanie 8')
x = np.arange(1, 9 * 5, 5).reshape(3, 3)
print(x)
for i in x:
    print(i)
    print("")

print('Zadanie 9')
x = np.arange(-10, -10 + 9 * 3, 3).reshape(3, 3)
print(x)
for i in x.flat:
    print(i)
    print("")

print('Zadanie 10')
x = np.arange(81).reshape(9, 9)
print(x)
print(x.shape)
print("")

# mamy 4 możliwości zmiany kształtu wliczając w to traspozycje

y = x.reshape(3, 27)
print(y)
print(y.shape)
print("")

z = y.reshape(1, 81)
print('\n', z)
print(z.shape)
print("")

e = y.T
print(e)
print(e.shape)
print("")

f = z.T
print(f)
print(f.shape)
print("")

print('Zadanie 11')
a = np.arange(12)
print(a)
print(a.shape)
print("")

b = a.reshape(3, 4)
print(b)
print(b.shape)
print("")

c = b.reshape(4, 3)
print(c)
print(c.shape)
print("")

d = c.reshape(2, 6)
print(d)
print(d.shape)
print("")

e = b.ravel()
print("Spłaszczenie macierzy 3x4\n", e)
print(e.shape)
print("")

e = c.ravel()
print("Spłaszczenie macierzy 4x3\n", e)
print(e.shape)
print("")

e = d.ravel()
print("Spłaszczenie macierzy 2x6\n", e)
print(e.shape)
print("")
# po spłaszczeniu macierze są identyczne do płaskiej pierwszej macierzy
