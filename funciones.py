import pandas as pd



df = pd.read_csv('synergy_logistics_database.csv')


def mejoresRutas():
    df_rutas = pd.concat ([df['origin'], df['destination']], axis = 1)
    print(df_rutas.value_counts()[:10])
    


def transporte():
    df_transporte = pd.concat([df['transport_mode'], df['total_value']], axis = 1)
    print(df_transporte.groupby('transport_mode').sum(),"\n")




def valor():
    df_valorT = pd.concat([df['origin'], df['total_value']], axis = 1)

    total_ordenado = df_valorT.groupby('origin').sum()
    print(total_ordenado.sort_values('total_value', ascending=0),"\n")
    