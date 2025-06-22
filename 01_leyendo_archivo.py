# Importamos pandas y leemos el registro de compras de una empesa denominada Tienda 12
 
import pandas as pd
import os

path = os.getcwd()

compras = pd.read_csv(path + r"/compras-abril.txt",delimiter = "|")
compras.head()

# Convertimos la fecha de emision y la fecha de vencimiento para que sean manipulables por pandas
compras['Fecha de emisión'] = pd.to_datetime(compras['Fecha de emisión'], format="%d/%m/%y", errors='coerce')
compras['Fecha Vcto/Pago'] = pd.to_datetime(compras['Fecha Vcto/Pago'], format="%d/%m/%y", errors='coerce')

# Concatenamos la columna serie del comprobante  y numero de comprobantes para crear la columna comprobante
compras["comprobante"] = (compras["Serie del CDP"].fillna("").astype(str) + "-" + compras["Nro CP o Doc. Nro Inicial (Rango)"].fillna("").astype(str))

# Calculamos el total de adquisiciones realizadas en cada proveedor
compras_totales = compras.groupby("Apellidos Nombres/ Razón  Social")["Total CP"].sum()

# Los 10 proveedores con mayor facturacion
print(compras_totales.sort_values(ascending=False).head(10))

# Importando la libreria matplotlib para visualizar graficos
import matplotlib.pyplot as plt
# %matplotlib inline

# Mostrando graficamente la adquisiciones del los 10 proveedores con mayor facturacion
compras_totales.sort_values(ascending=False).head(10).plot(kind = "bar", color = "orange",figsize =(10,5));
plt.title("Proveedores por Monto Facturado");
plt.xlabel("Proveedores");
plt.ylabel("Monto Facturado");