# Importamos os módulos que usaremos para este EP
import numpy as np
import matplotlib.pyplot as plt

# Definimos a função que queremos resolver numericamente
def func(x):
    return x**3 - np.cos(x)

# Geramos intervalos entre -10 e 10 de lagura 1
intervals = np.arange(-10, 10, 1)

# Verficamos em qual dele há raízes
intervals_found = []
for i in range(len(intervals) - 1):
    if func(intervals[i]) * func(intervals[i + 1]) < 0:
        intervals_found.append([intervals[i], intervals[i + 1]])

# Aplicamos o método da bissecção nos intervalos encotrados
epsolon = 0.0001
for interval in intervals_found:
    x1 = interval[0]
    x2 = interval[1]
    print('{:^10} {:^10} {:^10} {:^10} {:^10} {:^10} {:^10}'.format('x1', 'x2', 'xm', 'f(x1)', 'f(x2)', 'f(xm)', '|x2-x1|'))
    while np.abs(x2 - x1) > epsolon:
        xm = (x1 + x2) / 2
        print('{:<8.8f} {:<8.8f} {:<8.8f} {:<8.8f} {:<8.8f} {:<8.8f} {:<8.8f}'.format(x1, x2, xm, func(x1), func(x2), func(xm), np.abs(x2- x1)))
        if func(x1) * func(xm) > 0: x1 = xm
        if func(x2) * func(xm) > 0: x2 = xm
    print('Raíz entre: {}'.format([x1, x2]))

# Definimos analiticamente a derivada função e a adicionamos na forma de uma nova função
def der_func(x):
    return 3 * x**2 + np.sin(x)

# Iteramos pela definição de x no método de Newton-Raphson
x = 0.1
print('{:>3} {:>12} {:>16} {:>16}'.format('n', 'x_n', 'f(x_n)', 'df(x_n)'))
for i in range(10):
    x = x - func(x) / der_func(x)
    print('{:>3} {:>12.8f} {:>16.8f} {:>16.8f}'.format(i+1, x, func(x), der_func(x)))

# Definimos as constantes que usaremos para montar as funções:
const = 14.4    # eV A
V_0 = 1.09E3   # eV
r_0 = 0.330     # A

# Calculamos o potencial
r = np.arange(0.1, 10, 1E-2)
u = -const/r + V_0*np.exp(-r/r_0)

plt.figure(figsize=(15, 10))
plt.plot(r, u)
plt.title('Potencial versus distância')
plt.xlabel('Distância / [A]')
plt.ylabel('Energia potencial / [eV]')
plt.xlim(0, 10)
plt.ylim(-6, 4)
plt.grid(True)
plt.show()

# Calculamos a força
f = -const/r**2 + V_0*np.exp(-r/r_0)/r_0

plt.figure(figsize=(15, 10))
plt.plot(r, f)
plt.title('Força versus distância')
plt.xlabel('Distância / [A]')
plt.ylabel('Força / [eV/A]')
plt.xlim(0, 10)
plt.ylim(-2, 10)
plt.grid(True)
plt.show()

# Definimos a função da força
def force(x):
    return -const/x**2 + V_0*np.exp(-x/r_0)/r_0

# Aplicamos o método das secantes para encontrar o ponto onde a força é nula
'''
    x[0] -> x_n
    x[1] -> x_(n-1)
'''
x = (0.1, 0.2)
print('{:>3} {:>18} {:>24} {:>24} {:>24}'.format('n', 'x_n', 'f(x_n)', 'x_n-1', 'f(x_n-1)'))
for i in range(20):
    x = (x[0] - force(x[0])*(x[0]-x[1])/(force(x[0])-force(x[1])), x[0])
    print('{:>3} {:>18.14f} {:>24.14f} {:>24.14f} {:>24.14f}'.format(i+1, x[0], force(x[0]), x[1], force(x[1])))