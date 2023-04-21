"""
Este código es para realizar gráficos de
estadística descriptiva

"""

#%%Gráficos de barras
import pandas as pd
import matplotlib.pyplot as plt

data = pd.DataFrame({'España': [800, 943, 942, 901],
                     'México': [668, 781, 791, 813],
                     'colombia':[488, 553, 563, 537]},
                    index=('lunes','martes','miercoles','jueves'))      #Creación de la base de datos

#Diagrama de barras verticales para indicar el numero visitas totales por dia de la semana
total = data.sum(axis=1)     #suma de las filas para estimar las visitas totales por día de la semana
plt.bar(total.index, total)  #Se genera el gráfico de barras para el total de visitas por día
plt.show()                   #comando para indicar que he terminado la gráfica

#Diagrama de barras horizontales para indicar el numero visitas totales por dia de la semana
plt.barh(total.index, total)
plt.show()

#diagrama de barras verticales montadas para indicar las visitas totales y por país
plt.bar(data.index, data.España + data.México + data.colombia, label='España')  #Graficamos las barras con altura españa
plt.bar(data.index, data.México + data.colombia, label='México')
plt.bar(data.index, data.colombia, label='Colombia')
plt.legend(loc="best")
plt.show()

#diagrama de barras verticales adyacentes
import numpy as np

n=len(data.index)
x=np.arange(n)
width=0.2
plt.bar(x-width, data.España, width=width, label="España")
plt.bar(x, data.México, width=width, label="México")
plt.bar(x+width, data.colombia, width=width, label="Colombia")
plt.xticks(x, data.index)
plt.legend(loc='best')
plt.show()

#%% gráfico circular

"""
Para ejemploficar la realización de gráficos de torta
vamos a suponer que se tienen datos de personas
poseen cierta cantidad de manzanas

"""
from matplotlib import cm
from matplotlib import colors

Manzanas = [20,10,25,30]
nombres = ["Ana","Juan","Diana","Catalina"]

normdata = colors.Normalize(min(Manzanas),max(Manzanas))
colormap = cm.get_cmap("Blues")
colores = colormap(normdata(Manzanas))
desfase = (0,0,0,0.2)

plt.pie(Manzanas, labels=nombres, autopct="%0.1f%%", colors=colores, explode=desfase)
plt.axis("equal")
plt.show()

#%%diagrama de Pareto

#Create dataframe
df=pd.DataFrame({'Frecuencia': [4,6,30,6,4,5,5,21]})
df.index = ["Abolladuras","Agujeros","fuera de perfil",
            "Fuera de secuencia","Otros","Partes no lubricadas",
            "Piezas con rebabas","Piezas desordenadas"]

#Organizar los datos en orden descendente
df = df.sort_values(by="Frecuencia",ascending=False)  #Este comando organiza los datos de la columan Frecuencia de mayor a menor

#add column to display cumulative percentage
df['Frecuencia.R.Acum']=df["Frecuencia"].cumsum()/df["Frecuencia"].sum()*100

#librerías auxiliares
from matplotlib.ticker import PercentFormatter

#definir las estéticas para el gráfico
color1="steelblue"
color2="red"
line_size=4

#Create basic bar plot
fig, ax=plt.subplots()
ax.bar(df.index, df["Frecuencia"], color=color1)

#add cumulative percentage line plot
ax2 = ax.twinx()
ax2.plot(df.index, df['Frecuencia.R.Acum'],color=color2, marker="D", ms=line_size)
ax2.yaxis.set_major_formatter(PercentFormatter())


#colores de ejes
ax.tick_params(axis='y', colors=color1)
ax2.tick_params(axis='y',colors=color2)

plt.show()

#%%Tabla de Frecuencia para histograma

DataBase=pd.read_excel("C:\\Users\\sarango\\OneDrive - UCO\\Documentos\\UCO\\Cursos\\Estadística II\\Clases\\Ejemplos clases\\DescripciongraficadeDatosExcel.xlsx", sheet_name="Ejemplo")

#parámetros para la construcción de la tabla de frecuencia
Database = DataBase["datos"]

def TablaDeFrecuencia(Database):
    N=len(DataBase)
    L=int(round(pow(N,1/2),0))
    Min=min(Database)
    Max=max(Database)
    Tclase=(Max-Min)/L
    
    TablaFrecuencia=pd.DataFrame()
    
    clasesv=[]
    Infv=[]
    Supv=[]
    Frecuencias=[]
    FrecuenciaRv=[]
    Inf=Min
    Sup=Inf+Tclase
    
    
    for i in range (L):
        clasesv.append(i)
        count=0
        for element in Database:
            if Inf<=element<Sup+0.0001:
                count=count+1
        Frecuencias.append(count)
        FrecuenciaR=count/N
        FrecuenciaRv.append(FrecuenciaR)
        Infv.append(Inf)
        Supv.append(Sup)
        Inf=Sup
        Sup=Inf+Tclase
    
    TablaFrecuencia["clases"]=clasesv
    TablaFrecuencia["Inf"]=Infv
    TablaFrecuencia["Sup"]=Supv
    TablaFrecuencia["Frecuencia"]=Frecuencias
    TablaFrecuencia["FrecuenciaR"]=FrecuenciaRv
    
    hist=plt.hist(Database, bins=L, range=(Min, Max))
    plt.xlabel("Clases")
    plt.ylabel("Frecuencia")
    
    return TablaFrecuencia, hist

Tabla=TablaDeFrecuencia(Database=Database)[0]
Hist= TablaDeFrecuencia(Database=Database)[1]
plt.show()

#%%Diagrama de caja 

Cajaybigotes=plt.boxplot(Database, vert=False)
plt.show()


#%%Estadística descriptiva numérica
import statistics as st

Xbarra=st.mean(Database)    
DesvEst=st.stdev(Database)
Varianza=DesvEst**2
Q=st.quantiles(Database)
Q1=Q[0] 
Q3=Q[2]

RangoIntercuartilico=Q3-Q1  










