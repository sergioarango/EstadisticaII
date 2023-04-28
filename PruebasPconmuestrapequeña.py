# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 20:31:38 2023

@author: Sergio
"""
from scipy.stats import binom
import pandas as pd

Po=0.9
n=20
Pxv=[]
xv=[]
Fx=0
alfa=0.05

fmpbinom=pd.DataFrame()

for i in range (n+1):
    Px=binom.pmf(i, n, Po, loc=0)
    Pxv.append(Px)
    xv.append(i)
    Fx=Fx+Px
    if Fx<alfa:
        C=i
        Error=Fx
      
print(str(C)+" Cumple con la condición")    
print("el error verdadera sería "+str(round(Error*100,2))+"%")   
print("La región de rechazo serian aquellas muestras donde menos de " +str(C)+" Botes No pasen la prueba") 
    
fmpbinom["x"]=xv
fmpbinom["Px"]=Pxv