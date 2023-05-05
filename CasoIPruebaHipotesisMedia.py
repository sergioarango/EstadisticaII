# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:32:46 2023

@author: sarango
"""

from scipy.stats import norm
import math as mt

Do=0
Xbarra=48.9
Ybarra=43.2
n=125
m=90

sigma1=14.6
sigma2=14.4

alfa=0.05

Z=(Xbarra-Ybarra)/(mt.sqrt(((sigma1**2)/n)+((sigma2**2)/m)))

#Prueba de hipótesis con valores Z
Zalfa=norm.ppf(1-alfa)
if Z>Zalfa:
    print("Se rechaza la hipótesis nula, es decir la media de edad de los médicos es superior a la de los médicos académicos")
else:
    print("No se rechaza la hipótesis nula, es decir, la media de edad de los médios practicantes No es superior a la de los académicos")

















