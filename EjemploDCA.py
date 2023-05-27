# -*- coding: utf-8 -*-
"""
Created on Fri May 19 18:46:37 2023

@author: sarango
"""

import pandas as pd
import numpy as np
from scipy.stats import f
from itertools import combinations      #Esta herramienta nos permite realizar las combinaciones de las medias para el método LSD
from scipy.stats import t
import matplotlib.pyplot as plt
from scipy.stats import shapiro

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

#Método LSD para identificar los tratamientos diferentes estadísticamente hablando
medias=Data["medias"].tolist()          #volvemos la columna de medias de la tabla de datos una lista
comb = combinations(medias,2)

TablaLSD=pd.DataFrame()      #Aquí consignamos los resultados del método LSD
Parejas=[]
diferencia = []
conclusion = []
nombres=list(range(0,4))
ParejasNombre = []

combNombres=combinations(nombres,2)

talfa=-t.ppf(0.025,N-k)
LSD=talfa*np.sqrt(CME*((1/n)+(1/n)))

for i in list(comb):
    Parejas.append(i)
    diferencia.append(abs(i[0]-i[1]))
    if abs(i[0]-i[1])>=LSD:
        conclusion.append("Significativa")
    else:
        conclusion.append("No significativa")

TablaLSD["Parejas"]=Parejas
TablaLSD["diferencia"]=diferencia
TablaLSD["Conclusion"]=conclusion

print(TablaLSD)

#Gráfico de medias

intervaloC=talfa*np.sqrt(CME/(N/2))

for i in range (k):
    media=medias[i]
    Isup=media+intervaloC
    Iinf=media-intervaloC
    plt.plot([i,i,i],[Iinf,media,Isup], linewidth=2,marker=".", color="black")

new_list = range(0, 3+1)                 #Esto es para quitar los decimales del eje x
plt.xticks(new_list)                     
plt.xlabel("tratamientos")               #Nombres a los ejes
plt.ylabel("Tiempo de ensamble [min]")   #Nombres a los ejes
plt.show()                               #termino la gráfica

#Verificación de normalidad método de shapiro wilks
#1. necesitamos una lista con todos los datos de matriz del DDE
DataNormal=pd.DataFrame()
DataNormal["Data"]=Data[1].tolist()+Data[2].tolist()+Data[3].tolist()+Data[4].tolist()

#2 Se realiza se realiza la prueba de shapiro Wilks con la funcion Shapiro de scipy
Shapiro=shapiro(DataNormal["Data"])

#Se imprime el valor de W calculado y el valor P
print("El valor de W calculaso es: ",Shapiro[0])
print("El valor P para el W calculado en la prueba de shapiro es: ",Shapiro[1])

if Shapiro[1]<0.05:
    print("Se rechaza normalidad de los residuos")
else:
    print("No se rechaza normalidad de los residuos el ANOVA es valido en cuestión de normalidad")

#prueba gráfica de normalidad
#1 necesito todos los datos en una sola columna
#2 Organizo los datos en orden ascendente, es decir de menor a mayor
DataNormal=DataNormal.sort_values("Data")
#3. Le asignamos a cada dato una posición
i=list(range(1,len(DataNormal)+1))    #creamos una lista con las posiciones
DataNormal["i"]=i                     #Anexamos las posiciones al DataFrame de data normal

#4. Calculamos con esta función el papel de probabilidad normal
def NormalOperation(x):
    global N
    return (x-0.5)/N     #i-0.5/N

DataNormal["(i-0.5)/N"]=DataNormal["i"].apply(lambda x: NormalOperation(x))  #aplica a cada valor de la columna i la misma función que esta programada en la función Normal Operation

plt.plot(DataNormal["Data"],DataNormal["(i-0.5)/N"],"bo")
plt.xlabel("ri")
plt.ylabel("(i-0.5)/N")
plt.show()































