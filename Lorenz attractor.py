import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Аттрактор Лоренца

s, r, b = 10, 28, 8/3   # Коэффициенты sigma, rho и beta
def f(a, t):
 x, y, z = a
 return [s*(y-x), -y+(r-z)*x, -b*z+x*y]   # Система уравнений
t = np.linspace(0,20,2000)

y0 = [1, 1, 2]   # Начальные условия в первом случае
[x, y, z] = odeint(f, y0, t, full_output=False).T
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.5)
ax.set_title('Начальные условия y0 = [1, 1, 2]')
plt.xlabel('x')
plt.ylabel('y')

y0 = [1, 1, 2.0001]   # Начальные условия во втором случае
[x, y, z] = odeint(f, y0, t, full_output=False).T
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.5)
ax.set_title('Начальные условия y0 = [1, 1, 2.0001] ')
plt.xlabel('x')
plt.ylabel('y')

plt.show()




