import streamlit as st
import pandas as pd
import numpy as np
from datetime import date, time, datetime, timedelta
from PIL import Image
import plotly as plt
import plotly.express as px
import plotly.figure_factory as ff
import plotly.graph_objects as go

#Importamos la imagen del titulo
image1 = Image.open('contaayuda.jpg')
image2 = Image.open('TEC.png')
#La asignamos en el titulo
col1, col2 = st.columns([3,1])
with col1:
    st.image(image1)
with col2:
    st.image(image2)
#Leemos nuestro DataFrame
df = pd.read_csv('TEMPXMLFILEDATA.csv')
#Seleccionamos el cliente al que le haremos el análsiis
st.sidebar.header("Tablero: MONTY")
cliente = st.sidebar.selectbox("NÚMERO DE CLIENTE:",pd.Series(df['CUSTOMERID'].unique()).sort_values())
#Filtramos nuestros datos a ese cliente y agarramos las columnas de interés
df2 = df[df['CUSTOMERID'] == cliente][['XMLFILEID','DATE','CREATEDBY','RECEIVEDBY','TOTALBEFORTAX',
                                      'VATAMT','VATAMOUNT', 'INCOMETAXAMT', 
                                      'TOTALAFTERTAX','TRANSACTIONID',
                                      'INVOICETYPE','PAYMETHODCODE',
                                      'TOTALREGISTERTAX']].copy()
#Hacemos un trabajo de limpieza a las columnas
df2['INVOICETYPE'] = df2['INVOICETYPE'].replace(['P'], 'pago')
df2['INVOICETYPE'] = df2['INVOICETYPE'].replace(['p'], 'pago')
df2[['VATAMT','VATAMOUNT','INCOMETAXAMT']] = df2[['VATAMT','VATAMOUNT',
                                                  'INCOMETAXAMT']].fillna(0)
df2['TOTALREGISTERTAX'] = df2['VATAMOUNT'] + df2['INCOMETAXAMT']
df2['DATE'] = pd.to_datetime(df2['DATE'],format='%Y-%m-%d %H:%M:%S')
df2['AÑO'] = pd.to_datetime(df2['DATE']).dt.year
df2['MES'] = pd.to_datetime(df2['DATE']).dt.month
df2['DIA'] = pd.to_datetime(df2['DATE']).dt.day
#df2['AÑOMES'] = (((pd.to_datetime(df2['DATE']).dt.year)-2000)*100 + df2['MES'] = pd.to_datetime(df2['DATE']).dt.month)
tab1, tab2, tab3 = st.tabs(["BIENVENIDA", "FACTURAS", "IMPUESTOS"])

#Bienvenida
with tab1:
    #Generamos la fecha del día de hoy y confirmamos el cliente al que le estamos haciendo el análisis
    col1, col2 = st.columns([2,1])
    with col1:
        st.header("Bienvenido Cliente: #")
    with col2:
        st.header(cliente)
    #Creamos un texto explicativo para mostrar algunos de los valores que tenemos de ese cliente
    st.write("DESPLEGAMOS LAS ÚLTIMAS FACTURAS REGISTRADAS:")
    number = st.number_input('Facturas a visualizar: ',min_value=1,value = df2.tail().count()['DATE'])
    st.dataframe(df2.tail(number))
    
    st.write("Información actualizada al",datetime.now().date())
    

#FACTURAS
with tab2:
    #Genero el slider de cada año
    if df2['AÑO'].min() == df2['AÑO'].max():
        anio1 = st.slider("AÑO",(df2['AÑO'].min()-1),df2['AÑO'].max(), value = df2['AÑO'].max(),key = '1')
    else:
        anio1 = st.slider("AÑO",df2['AÑO'].min(),df2['AÑO'].max(),value = df2['AÑO'].max(),key = '1')
    dummy = df2[df2['AÑO'] == anio1]
    col1, col2 = st.columns([5,1])
    with col1:
        opr1 = st.selectbox("Operación a aplicar sobre las Facturas por mes:",("Suma","Promedio","Conteo"))
        #Creamos un Pie Chart donde podemos ver la suma/promedo/conteo de las facturas pagadas por ese cliente
        if opr1 == "Suma":
            gra1 = dummy.groupby('MES').sum()
        elif opr1 == "Promedio":
            gra1 = dummy.groupby('MES').mean()
        else:
            gra1 = dummy.groupby('MES').count()
        fig = px.pie(gra1,values = 'TOTALAFTERTAX',names = gra1.index, color_discrete_sequence=px.colors.sequential.haline,title = "Facturas en composición por Mes")
        st.plotly_chart(fig, use_container_width=True)
        #Creamos un Pie Chart donde podemos ver las facturas pagadas por ese cliente
        gra3 = dummy.groupby('PAYMETHODCODE').count()
        fig = px.pie(gra3,values = 'INVOICETYPE',names = gra3.index, color_discrete_sequence=px.colors.sequential.haline,title = "Facturas pagadas en una exhibición (PUE) vs diferidas (PPD)")
        st.plotly_chart(fig, use_container_width=True)
        
        fig6 = px.bar(df2[df2['AÑO'] == anio1],x = 'MES', y = 'TOTALAFTERTAX', color = 'INVOICETYPE', barmode = 'group',color_discrete_sequence=px.colors.sequential.haline,title = "Comparación de Ingresos y Egresos de las Facturas por Mes")
        st.plotly_chart(fig6, use_container_width=True)
    with col2:
        #Obtenemos el número de Facturas generadas por el cliente
        st.subheader("TOTAL DE FACTURAS GENERADAS:")
        st.metric(label = "",value = df2['XMLFILEID'].count(), delta = int(5000 - df2['XMLFILEID'].count()),help="Arriba (en negro) se muestran: FACTURAS GENERADAS. Abajo (en verde o rojo) se cuentan: FACTURAS RESTANTES EN SU PAQUETE")
    
#IMPUESTOS
with tab3:
    #Genero el slider de cada año
    if df2['AÑO'].min() == df2['AÑO'].max():
        anio2 = st.slider("AÑO",(df2['AÑO'].min()-1),df2['AÑO'].max(), value = df2['AÑO'].max(),key = '2')
    else:
        anio2 = st.slider("AÑO",df2['AÑO'].min(),df2['AÑO'].max(),value = df2['AÑO'].max(),key = '2')
    dummy = df2[df2['AÑO'] == anio2]
    #Creamos una línea de tiempo donde podemos ver la suma/promedio/conteo de las facturas pagados por ese cliente
    opr2 = st.radio("Operación a aplicar sobre los impuestos:",("Suma","Promedio","Conteo"))
    col1, col2= st.columns([7,1])
    with col1:
        if opr2 == "Suma":
            gra2 = dummy.groupby('MES').sum()
        elif opr2 == "Promedio":
            gra2 = dummy.groupby('MES').mean()
        else:
            gra2 = dummy.groupby('MES').count()
        fig2 = px.line(gra2,x=gra2.index,y = 'TOTALREGISTERTAX')
        fig2.update_traces(line_color = "green", line_width=5)
        st.plotly_chart(fig2, use_container_width=True)
        #Creamos una línea de tiempo donde podemos ver la suma/promedio/conteo del IVA y del ISR
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(x=gra2.index,y = gra2['VATAMOUNT'],name = "IVA",line=dict(color = '#3e67ec')))
        fig3.add_trace(go.Scatter(x = gra2.index, y = gra2['INCOMETAXAMT'],name = "ISR",line=dict(color ='#060e66')))
        st.plotly_chart(fig3, use_container_width=True)
    with col2:
        #Obtenemos el Total de impuestos pagados por el cliente
        st.subheader("TOTAL DE IMPUESTOS PAGADOS:")
        st.header("${:,.2f}".format(dummy['TOTALREGISTERTAX'].sum()))