"""
Created on Fri Apr 21 17:09:35 2023

@author: sarango
Pruebas de hipótesis caso III
"""
#%%Librerías
import pandas as pd
from scipy.stats import t
from scipy.stats import norm
import statistics as st 
import math

#%%Datos
Data=pd.read_excel(r'C:\Users\sarango\OneDrive - UCO\Documentos\UCO\Cursos\Estadística II\Clases\Ejemplos clases\PruebaDeHipotesisCasoIII.xlsx', sheet_name="Hoja1")

#%%Preuba de hipótesis para la media Caso III

#definción de la hipotesis nula
miu=10
alfa=0.05
Xbarra=st.mean(Data["Datos"])
S=st.stdev(Data["Datos"])
n=len(Data["Datos"])

tcalc=(Xbarra-miu)/(S/math.sqrt(n))
tcritica=-t.ppf(alfa,n-1)

if tcalc>tcritica:
    print("Se rechaza Ho a favor de Ha")
else:
    print("No se rechaza Ho")

#%%Prueba de hipótesis con valores P

miu=245
alfa=0.01
Xbarra=246.19
S=3.60
n=50

Zcalc=(Xbarra-miu)/(S/math.sqrt(n))
fizcalc=norm.cdf(Zcalc)
P=2*(1-fizcalc)

if P>alfa:
    print("No se rechaza Ho")
else:
    print("Se rechaza Ho a favor de Ha")




