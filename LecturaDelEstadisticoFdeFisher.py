# -*- coding: utf-8 -*-
"""
Encuentre el valor de F a la derecha  con un alfa de 0.05. con 𝜈_1=6 y 𝜈_2=10 

@author: sarango
"""
alfa=0.05
v_1=6
v_2=10
from scipy.stats import f
F11=f.ppf(alfa,v_2,v_1)
F=1/F11

print("el percentil de F a un alfa de 0.05 en el lado derecho de la gráfica es : "+str(F))

F12=f.ppf(alfa,v_1,v_2)

print("el percentil de F a un alfa de 0.05 en el lado izquierdo de la gráfica es :"+str(F12))