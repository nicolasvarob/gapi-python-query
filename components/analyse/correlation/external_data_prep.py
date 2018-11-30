import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('external-data/totales_diarios.csv',header=0)
df['Fecha de Venta'] = pd.to_datetime(df['Fecha de Venta'])

""" df = df.drop(['Unnamed: 0'],axis=1)
filter = df['Fecha de Venta'].str.contains('(?i).*Total.*')
df = df[~filter]

## Limpia la data 
df_cl = df.drop(columns=['Mi Mascota','Total Venta']).replace(to_replace='.*-.*|.*x.*',value=0, regex=True).fillna(0)
df_cl = df_cl[df_cl.columns.drop(list(df_cl.filter(regex='SOAP.*')))]

df_cl['Ventas totales'] = df['SeguroxKM'] + df['Auto Flexible'] + df['RCI Mercosur (Ex RC Argentina)'] + df['Asistencia en Viaje'] + df['Enfermedades']

print(df_cl)

external_data = df_cl """

external_data = df