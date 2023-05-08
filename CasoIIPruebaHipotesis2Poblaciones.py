# -*- coding: utf-8 -*-
"""
Created on Fri May  5 18:50:16 2023

@author: sarango
"""
import pandas as pd
import statistics as st
from scipy.stats import norm
import math

Data=pd.read_excel(r'C:\Users\sarango\OneDrive - UCO\Documentos\EstadisticaII\DatosBombillas.xlsx',sheet_name="Data")
DataPhilips=Data["Philips"].tolist()
DataTopluz=Data["Topluz"].tolist()

n=len(DataPhilips)
m=len(DataTopluz)
Xbarra=st.mean(DataPhilips)
Ybarra=st.mean(DataTopluz)
S1=st.stdev(DataPhilips)
S2=st.stdev(DataTopluz)
alfa=0.01

Z=(Xbarra-Ybarra)/(math.sqrt((S1**2/n)+(S2**2/m)))

#Prueba de hipótesis con valores P
P=1-norm.cdf(Z)

if P<alfa:
    print("Se rechaza la hipótesis nula, es decir la duración de la bombillas philips es superior a las bombillas Topluz")
else:
    print("No se rechaza la hipótesis nula, es decir la duración de ambas bombillas es estadisticamente igual")

#Con valores Z
Zalfa=norm.ppf(1-alfa)

if Z>Zalfa:
    print("Se rechaza la hipótesis nula, es decir la duración de la bombillas philips es superior a las bombillas Topluz")
else:
    print("No se rechaza la hipótesis nula, es decir la duración de ambas bombillas es estadisticamente igual")


