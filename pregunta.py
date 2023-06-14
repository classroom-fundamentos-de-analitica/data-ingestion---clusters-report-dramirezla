"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import re
import pandas as pd


def ingest_data():
    with open('clusters_report.txt') as doc:
        reporte = doc.readlines()
    agrups=[]
    agrup1=[0,0,0,'']
    for row in reporte[4:]:
        if re.match('^ +[0-9]+ +', row):
            lista=row.split()
            agrup1=[int(lista[0]),int(lista[1]),float(lista[2].replace(',','.')),' '.join(lista[4:])]

        elif re.match('^ +[a-z]',row):
            palabras=' '.join(row.split())
            agrup1[3]+=' '+palabras

        elif re.match('^\n|^\s*$',row):
            agrup1[3]=agrup1[3].replace('.','')
            
            agrups.append(agrup1)
            agrup1=[0,0,0,'']

    df=pd.DataFrame(agrups,columns=['cluster','cantidad_de_palabras_clave','porcentaje_de_palabras_clave','principales_palabras_clave'])
    
    return df
