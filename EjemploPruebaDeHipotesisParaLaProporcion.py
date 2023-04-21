# -*- coding: utf-8 -*-
"""
Prueba de hipotesis para la proporcion
Ejemplo 1
"""
#%%librerías
from scipy.stats import norm
import statistics
import math

#%%Prueba de hipotesis para la proporción
Po=1.5*0.2
Pgorro=1276/4115
n=4115
Z=(Pgorro-Po)/math.sqrt((Po*(1-Po))/n)
alfa=0.1

#Prueba de hipotesis con valores P
fiz=norm.cdf(Z)
P=1-fiz

if P>alfa:
    print("No se rechaza Ho")
else:
    print("Se rechaza Ho")
    
#Prueba de hipotesis con valores Z
Zcritico=-norm.ppf(alfa)

if Z<Zcritico:
    print("No se rechaza Ho")
else:
    print("Se rechaza Ho")









