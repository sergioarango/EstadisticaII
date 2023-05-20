# -*- coding: utf-8 -*-
"""
Created on Fri May 19 18:46:37 2023

@author: sarango
"""

import pandas as pd
import numpy as np
from scipy.stats import f

Data=pd.read_excel(r'C:\Users\sarango\OneDrive - UCO\Documentos\EstadisticaII\datosunifactorial.xlsx', sheet_name="Hoja1")    #Traemos los datos del experimento

yij2=np.square(Data)           #elevamos al cuadrado cada observación de la matriz       
yij2["total"]=yij2.sum(axis=1) #sumamos los cuadrados de cada tratamiento
sumayij2=sum(yij2["total"])    #Estimamos la sumacuadrado de todas las observaciones de la matriz de datos
k=len(Data.index)              #Calculamos el número de tratamientos contando el número de filas en la matriz de datos (Data)
n=len(Data.columns)            #Contamos el numero de observaciones por tratamiento contando las columnas de la matriz de datos
N=k*n                          #encontramos el numero total de observaciones
Data["medias"]=Data.mean(axis=1)  #encontramos las medias de cada tratamiento y la añadimos a la matriz de datos
Data["Total"]=Data[1]+Data[2]+Data[3]+Data[4]  #Calculamos y añadimos la columna de totales a nuestra matriz de datos

Totales=Data["Total"].tolist()    #convertirmos la columna de  totales en una lista
ytotal=sum(Data["Total"])         #Calculamos y.. sumando los elementos de la columna de totales

SUMACUADRADOSYi=0
for i in range (k):                                  #Aquí calculamos la suma cuadrados de los yi.^2
    SUMACUADRADOSYi=SUMACUADRADOSYi+Totales[i]**2

SSTra=(1/n)*SUMACUADRADOSYi-((ytotal**2)/N)         #Se calcula la suma de cuadrados para los tratamientos
SST=sumayij2-((ytotal**2)/N)                        #Se calcula suma de cuadrados total
SSE=SST-SSTra                                       #Se calcula suma de cuadrados de los tratamientos

#Caculamosla varianzas
#1 definir los grados de libertad
GLtra=k-1
GLT=N-1
GLE=N-k

#2Calcular las varianzas
CMTra=SSTra/GLtra                                #Varianza para los tratamientos
CME=SSE/GLE                                      #Varianza para el error
CMT=SST/GLT                                      #Varianza total

#Prueba de hipotesis
#1 calcular F
Fcalc=CMTra/CME               

#2Valor P para la prueba de hipótesis
P=1-f.cdf(Fcalc,GLtra,GLE)

print("El valor F para el experimento es: "+str(Fcalc))
print("El valor P para la Fcalc es: "+str(P))



