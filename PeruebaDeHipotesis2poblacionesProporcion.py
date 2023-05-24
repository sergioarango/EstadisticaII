# -*- coding: utf-8 -*-
"""
Prueba de hipótesis dos poblaciones proporción

@author: sarango
"""
import numpy as np
from scipy.stats import norm

P1muestral=0.875
q1m=1-P1muestral
m=191
X=101

P2muestral=0.529
q2m=1-P2muestral
n=65
Y=56

Pgorro=(m/(m+n))*P1muestral+(n/(m+n))*P2muestral
Qgorro=1-Pgorro

Z=(P1muestral-P2muestral)/(np.sqrt(Pgorro*Qgorro*((1/m)+(1/n))))

#Prueba de hipótesis con valores P
P=2*(1-norm.cdf(Z))

alfa=0.05
#conclusión
if P<=alfa:
    print("Se rechaza Ho, es decir, la probabilidad de declararse culpable e ir prisión es diferente de la probabilidad de declararse inocente e ir prisión")
else:
    print("No se rechaza Ho, es decir, La probabilidad de declarase culpable e ir a prisión es la misma que declarse inocente e ir a prisión")

"""
Resolver el ejercicio con valores Z
"""

