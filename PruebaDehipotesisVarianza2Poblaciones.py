# -*- coding: utf-8 -*-
"""
Prueba de hipótesis para la varianza

@author: sarango
"""
from scipy.stats import f

S1=52.6
S12=(52.5)**2
m=26

S2=84.2
S22=(84.2)**2
n=28

fcalc=S12/S22
alfa=0.05
#Calculo el valor de Fcritico
Fcritico=1/f.ppf(alfa,n-1,m-1)

#conclusion
if fcalc<Fcritico:
    print("Se rechaza Ho, es decir, la desviación del consumo de farmacos en adultos jovenes es menor que la del consumo en adultos mayores")
else:
    print("No rechazar Ho, es decir, la desviación de consumo de farmacos en adultos jovenes es igual a la desviación de consumo de farmacos en adultos mayores")

