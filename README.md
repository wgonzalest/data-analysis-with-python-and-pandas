# Analisis de Datos con Python + Pandas

<img alt="Pandas Logo" src="https://pandas.pydata.org/static/img/pandas.svg" align="left" width="400px" height="230px" >
<img align="left" width="0" height="230px" hspace="10"/>

> P

> y

> t

> h

> o

> n

---

## 🧾 Contenido
- [Descripción del Proyecto](#-descripción-del-proyecto)
- [Objetivos del Proyecto](#-objetivos-del-proyecto)
- [Tecnologías y Librerías Utilizadas](#-tecnologías-y-librerías-utilizadas)
- [Contenidos del Repositorio](#-contenidos-del-repositorio)
- [Descripción del Proceso Realizado](#-descripción-del-proceso-realizado)
- [Resultados Obtenidos](#-resultados-obtenidos)
- [Posibles Mejoras Futuras](#-posibles-mejoras-futuras)

---

## 💼 Descripción del Proyecto

En este proyecto se realiza un análisis del registro de compras del mes de abril de la empresa **Tienda 12** utilizando Python y las librerias `pandas` y `matplotlib`. El objetivo principal de este pequeño proyecto es identificar los proveedores con mayor facturación y presentar la información de forma clara y visualmente comprensible.

---

## 🎯 Objetivos del Proyecto

- Acceder y leer el archivo de compras en formato `.txt` delimitado por `|`.
- Convertir las columnas de fecha para su manipulación con `pandas`.
- Crear una nueva columna de identificación de comprobantes.
- Agrupar los datos por proveedor y calcular el total de adquisiciones.
- Identificar los 10 proveedores con mayor facturación.
- Visualizar los resultados mediante gráficos de barras.

---

## 📊 Tecnologías y Librerías Utilizadas

- Python Versión 3.13.2
- pandas
- matplotlib
- os (módulo estándar)
- Jupyter Notebook (para visualización interactiva)

---

## 📁 Contenidos del Repositorio

- 📦 compras-tienda12
- ┣ 📄 compras-abril.txt `(Archivo de datos fuente)`
- ┣ 📄 01_leyendo_archivo.ipynb `(Script del análisis con pandas en jupyter)`
- ┣ 📄 01_leyendo_archivo.py `(Script de análisis con pandas)`
- ┣ 📄 README.md `(Documentación del proyecto)`

---

## 🔍 Descripción del Proceso Realizado

### 1. Carga y Exploración de Datos
- Se utilizó `pandas.read_csv` para cargar el archivo `compras-abril.txt`.
- Se especificó el delimitador `|` al ser un archivo separado por palotes.

### 2. Limpieza y Preparación de Datos
- Se convirtio las columnas de fecha (`Fecha de emisión` y `Fecha Vcto/Pago`) al formato `datetime`.
- Manejo de posibles errores con `errors='coerce'` para evitar fallas.

### 3. Creación de Columna "comprobante"
- Se concatenó la serie del comprobante con el número del comprobante para formar un identificador único.

### 4. Análisis por Proveedor
- Se agruparon los datos por razón social del proveedor.
- Se calculó la suma del monto facturado (`Total CP`) por cada proveedor.

### 5. Visualización de Resultados
- Se generó un gráfico de barras con los 10 proveedores de mayor facturación.
- Se utilizó `matplotlib` para mostrar el gráfico de forma clara y profesional.

---

## 📈 Resultados Obtenidos

En este análisis se puede evidenciar aquellos proveedores más relevantes en términos de facturación para **Tienda 12**. Esta información resulta de suma importancia si se quiere optimizar las relaciones comerciales y enfocar mejor la gestión de abastecimiento.

---

## 🚀 Posibles Mejoras Futuras

- Agrupar compras por tipo de comprobante o categoría de gasto.
- Analizar la variación temporal (dias o semanas).
- Identificar comprobantes con montos inusuales.
- Exportar reportes a Excel o PDF.
- Construir  un dashboard interactivo con  Power BI.

---

## 👨‍💻 Autor
- William Gonzales Tarazona
- 📧 wgonzales.tarazona@gmail.com
- 🔗 www.linkedin.com/in/wgonzalest
- [![Wgonzalest](https://img.shields.io/badge/William_Gonzales_Tarazona-LinkedIn-blue.svg)](https://www.linkedin.com/in/wgonzalest/)
