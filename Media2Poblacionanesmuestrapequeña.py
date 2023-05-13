# -*- coding: utf-8 -*-
"""
Prueba de hipótesis para la media 2 poblaciones muestra pequeña

@author: sarango
"""
import pandas as pd
import numpy as np
import math as mt
from scipy.stats import t

Data=pd.read_excel(r'C:\Users\sarango\OneDrive - UCO\Documentos\EstadisticaII\Datos2poblacionesMuestrapequeña.xlsx', sheet_name="Hoja1")

n=len(Data["Xbienrecordado"])
m=len(Data["Ymalrecordado"])
Xbarra=Data["Xbienrecordado"].mean()
Ybarra=Data["Ymalrecordado"].mean()
S12=Data["Xbienrecordado"].var()
S22=Data["Ymalrecordado"].var()

tcalc=(Xbarra-Ybarra)/(np.sqrt((S12/n)+(S22/m)))

#estimación de los grados de libertad
nu=((S12/n)+(S22/m))**2/(((S12/n)**2/(n-1))+((S22/m)**2/(m-1)))
nu=np.floor(nu)
nu=int(nu)

#t crítico a un valor de alfa de 0.05
alfa=0.05
tcritico=-t.ppf(0.05, nu)

#conclusión
if tcalc>=tcritico:
    print("Se rechaza Ho, es decir, los anuncios bien recordados tiene mayor actividad cerebral que los anuncios no recordados")
else:
    print("NO se rechaza Ho, es decir, los anuncios bien recordados tiene la misma actividad cerebral que los anuncios no recordados")

"""
Hacer esta actividad con valores P
"""
    







