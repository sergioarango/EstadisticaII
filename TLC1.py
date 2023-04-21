#ejercicio Usando el teorema del límite central

#%%Librerías
from scipy.stats import norm
import sympy
import math

#%%Parámetros del ejercicio
Xbarra=3.5
n=30

"""
Paso numero 1 encontrar E(x) o la media poblacional
a partir de la pdf
"""

miu=(3/(4*125))*(5**4)     #Aqui solucione la integral manual
ex2=(3/(5*125))*(5**5)     #Encuentro E(x^2) para encontrar la varianza
vx=ex2-(miu**2)
sigma=pow(vx,1/2)          #Desviación estándar

Z=(Xbarra-miu)/(sigma/math.sqrt(n))  #Empleamos el TLC
fiz=norm.pdf(Z,0,1)

print("La probabilidad de que el tiempo excedido sea menor a 3.5min es: "+str(fiz))

#%%Ejercicio para el teorema de la varianza

from scipy.stats import chi2
import matplotlib.pyplot as plt

n=20
S2=7
sigma2=7.5

Chi2Cal=((n-1)*S2)/(sigma2)

fiChi=chi2.pdf(Chi2Cal,n-1)

print("la probabilidad que la varianza sea menor a 7 es: "+str(fiChi) )

#Curva de Chi cuadrada
R=chi2.rvs(7.5, 0, 1, 10000)

plt.hist(R)














