
#Se importa la libreria 'Pandas'

import pandas as pd

#Se importa el archivo CSV a un Data frame 

df = pd.read_csv('synergy_logistics_database.csv')


def mejoresRutas():

    #se crea un nuevo data frame con los valores de las columnas 'origin' y 'destination'
    df_rutas = pd.concat ([df['origin'], df['destination']], axis = 1)
    #se imprimen las 10 primeras filas
    print(df_rutas.value_counts()[:10])

def transporte():
    #se crea un nuevo data frame con los valores de las columnas 'transport_mode' y 'total_value'
    df_transporte = pd.concat([df['transport_mode'], df['total_value']], axis = 1)
    #Se hace uso de la funcion groupby() para  agrupar los resultados segun su medio de transporte
    #y se pasa por la funcion .sum() para sumar los ingresos
    print(df_transporte.groupby('transport_mode').sum(),"\n")
    

def valor():
    #se crea un nuevo data frame con los valores de las columnas 'origin' y 'total_value'
    df_valorT = pd.concat([df['origin'], df['total_value']], axis = 1)
    #Se hace uso de la funcion groupby() para  agrupar los resultados segun el pais
    #y se pasa por la funcion .sum() para sumar los ingresos
    total_ordenado = df_valorT.groupby('origin').sum()

    #se imprimen los primero 9
    print(f"Los países con el 80 % \n{total_ordenado.sort_values('total_value', ascending=0)[:9]}\n")

    #Se crea un lista con los valor del data frame 'total_ordenado' 
    #y se pasa por la funcion .sum() para sacar el total de ingresos
    total_ingresos = total_ordenado.sum().to_list()
    print(f"El total de ingresos es: {total_ingresos[0]}\n",
        #se calcula el 80 %
        f"El 80 % de los ingresos es: {80 * (total_ingresos[0]) / 100}")


