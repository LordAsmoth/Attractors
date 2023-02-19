import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Аттрактор Рикитаке

a, m = 0.5, 0.5   # Параметры a и mu
def f(q, t):
 x, y, z = q
 return [-m*x+y*z, -m*y+x*(z-a), 1-x*y]   # Система уравнений
t = np.linspace(0,300,20000)

y0 = [1, 1, 2]   # Начальные условия в первом случае
[x, y, z] = odeint(f, y0, t, full_output=False).T
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.3)
ax.set_title('Начальные условия y0 = [1, 1, 2]')
plt.xlabel('x')
plt.ylabel('y')

y0 = [1, 1, 2.0001]   # Начальные условия во втором случае
[x, y, z] = odeint(f, y0, t, full_output=False).T
fig = plt.figure(facecolor='white')
ax = fig.add_subplot(111, projection='3d')
ax.plot(x, y, z, linewidth=0.3)
ax.set_title('Начальные условия y0 = [1, 1, 2.0001]')
plt.xlabel('x')
plt.ylabel('y')

plt.show()

