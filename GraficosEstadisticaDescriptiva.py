#Gráficos de estadística descriptiva en Python

#%% Gráfico de barras
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import colors
import statistics as st
from scipy.stats import kurtosis
from scipy.stats import skew


#Datos de visitas por país en una semana
data = pd.DataFrame({'España' : [826, 943, 942, 901],
                     'Colombia': [668, 781, 791, 813],
                     'México': [488, 553, 563, 537]},
                    index=('Lunes', 'Martes', 'Miercoles', 'Jueves')) #Creación de datos

#Diagrama de barras verticales para indicar las visitas totales a los paises en cada día de la semana
total = data.sum(axis=1)                                              #suma de las filas de la tabla de datos
plt.bar(total.index, total)                                           #Gráfico de barras para los días de la semana
plt.show()                                                            #comando para separar los gráficos

#Diagrama de barras verticales para indicar las visitas totales a los paises en cada día de la semana
plt.barh(total.index, total)                                          #Creación de gráfico de barras horizontales para los días de la semana
plt.show()                                                            #comando para separar los gráficos

#Diagrama de barras verticales montadas para indicar las visitas a los paises en cada día de la semana
plt.bar(data.index, data.España + data.Colombia + data.México, label='España')  #comando para graficar los datos de españa 
plt.bar(data.index, data.Colombia + data.México, label='Colombia')              #comando para graficar las visitas en colombia
plt.bar(data.index, data.México, label='México')                                #comando para graficar las visitas en México
plt.legend(loc='best')                                                          #comando para encontrar la mejor ubicación de la leyenda                                                     
plt.show()                                                                      #comando para indicar el fin del gráfico

#Diagrama de barras adyacentes verticales 
import numpy as np
n = len(data.index)                                                             #Asignar el numero de dias de la semana
x = np.arange(n)                                                                #Crea un vector con numeros ordenados de o a n-1                                                            
width = 0.2                                                                     #ancho que le deseo dar a las barras
plt.bar(x - width, data.España, width=width, label='España')                    #Creación de la barra de españa en la izquierda
plt.bar(x, data.Colombia, width=width, label='Colombia')                        #Creación de la barra de colombia en la mitad
plt.bar(x + width, data.México, width=width, label='México')                    #Creación de la barra de méxico en la derecha
plt.xticks(x, data.index)                                                       #Asignación de los nombres de las emana en el eje x
plt.legend(loc='best')                                                          #localización de la leyenda del gráfico 
plt.show()                                                                      #comando para dar final al gráfico

#%% Grafico circular

"""
Para ejemplificar la realización de gráficos de tortas en python vamos a suponer que se tienen datos sobre algunas personas
que tienen cierta cantidad de manzanas en su poder
"""

manzanas = [20,10,25,30]                                                               #datos de manzanas                                                      
nombres = ["Ana","Juan","Diana","Catalina"]                                            #Nombres e las personas

normdata = colors.Normalize(min(manzanas),max(manzanas))                               #Asignar color a las pedazos de la torta, el dato mas pequeño es mas claro, el dato mas grande es oscuro
colormap = cm.get_cmap("Blues")                                                        #Asigno el color a la tora, en este caso es azul
colores = colormap(normdata(manzanas))                                                 #Mapeos los colores
desfase=(0, 0, 0, 0.1)                                                                 #Asigno una tupla para los defases en los nombres, en este caso asigno un desfase de 0.1 al valor maximo

cric1 = plt.pie(manzanas, labels=nombres, autopct="%0.1f%%", colors=colores, explode=desfase)  #Creo el gráfico con los datos manzanas, asigno los nombres, autopct para asignar en porcentajes, colores, desfase
plt.axis("equal")                                                                              #comando para que el gráfico sea simétrico
plt.show()                                                                                     #mostrar el g´rafico 


#%% Pareto


#create DataFrame
df = pd.DataFrame({'count': [97, 140, 58, 6, 17, 32]})                                         
df.index = ['B', 'A', 'C', 'F', 'E', 'D']

#sort DataFrame by count descending
df = df.sort_values(by='count', ascending=False)

#add column to display cumulative percentage
df['cumperc'] = df['count'].cumsum()/df['count'].sum()*100


import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

#define aesthetics for plot
color1 = 'steelblue'
color2 = 'red'
line_size = 4

#create basic bar plot
fig, ax = plt.subplots()
ax.bar(df.index, df['count'], color=color1)

#add cumulative percentage line to plot
ax2 = ax.twinx()
ax2.plot(df.index, df['cumperc'], color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())

#specify axis colors
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y', colors=color2)

#display Pareto chart
plt.show()

#%% histrograma

#construcción de la tabla de frecuencia

#Bring data from sheet of Excel
Data=pd.read_excel('C:\\Users\\sarango\\OneDrive - UCO\\Documentos\\UCO\\Cursos\\Estadística II\\Clases\\Ejemplos clases\\DescripciongraficadeDatosExcel.xlsx', sheet_name="Datahist")
Data=Data["Datos minutos consumidos"]
N=len(Data)

def TablaDeFrecuencia (Data):
    
    #Histogram parameters
    N=len(Data)
    Min=min(Data)
    Max=max(Data)
    L=int(round(pow(N,1/2),0))
    Tclase=(Max-Min)/L
    
    TablaDeFrecuencia=pd.DataFrame()
    
    Clasesv=[]
    
        
    
    Inf=Min
    Sup=Inf+Tclase
    Frecuenciav=[]
    Infv=[]
    Supv=[]
    Frecuenciarv=[]
    
    for i in range (L):
        Clasesv.append(i)
        count=0
        for elem in Data:
            if Inf <= elem < Sup+0.0001:
                    count=count+1
        Frecuenciav.append(count)
        Frecuenciar=count/N
        Frecuenciarv.append(Frecuenciar)
        Infv.append(Inf)
        Supv.append(Sup)
        Inf = Sup
        Sup = Inf + Tclase
    
    TablaDeFrecuencia["clases"]=Clasesv
    TablaDeFrecuencia["Inf"]=Infv
    TablaDeFrecuencia["sup"]=Supv
    TablaDeFrecuencia["Frecuencia"]=Frecuenciav
    TablaDeFrecuencia["Frecuencia.R"]=Frecuenciarv
    
    
    
    hist=plt.hist(Data, bins=L, range=(min(Data), max(Data)))
    plt.xlabel("Clases")
    plt.ylabel("Frecuencia")
    

    return TablaDeFrecuencia, hist

res=TablaDeFrecuencia(Data=Data)
Tabla=res[0]
Hist=res[1]
plt.show()

#%% Grafico de ojiva


Tabla['cumperc'] = Tabla['Frecuencia'].cumsum()/Tabla['Frecuencia'].sum()*100   

dispersion=plt.plot(Tabla["Inf"],Tabla["cumperc"])
plt.scatter(Tabla["Inf"],Tabla["cumperc"])
plt.show()

#%% boxplot

plt.boxplot(Data, vert=False)
plt.show()

#%% Estadística descriptiva numérica

Xbarra = st.mean(Data)          #estimación de la media
DesVest = st.stdev(Data)        #Estimación de la desviación estándar
Q=st.quantiles(Data)            #Estimación de los cuartíles
Fs=Q[2]-Q[0]                    #rango intercuartílico
Kurtosis=kurtosis(Data)         #si Kurt >3 leptocútrica, <3 platicurtica, =3 meso
CoeficienteAsimetria=skew(Data)
CoeficienteVar=(DesVest/Xbarra)*100

print("resumen descriptivo")
print("Media: "+str(Xbarra))
print("Varianza: "+str(DesVest**2))
print("Desviación estándar: "+str(DesVest))
print("Cuartil 1: "+str(Q[0]))
print("Cuartil 2: "+str(Q[1]))
print("Cuartil 3: "+str(Q[2]))
print("Rango intercuartílico: "+str(Fs))
print("Kurtosis: "+str(Kurtosis))
print("Coeficiente de asimetría: "+str(CoeficienteAsimetria))
print("coeficiente de variación: "+str(CoeficienteVar)+"%")

