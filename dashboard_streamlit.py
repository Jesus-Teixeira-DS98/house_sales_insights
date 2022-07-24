import pandas as pd
import streamlit as st
import numpy as np
from plotly import express as px
from datetime import datetime

pd.set_option('display.float_format', lambda x: '%.2f' % x)
@st.cache( allow_output_mutation=True )

def get_data(path):
    data = pd.read_csv(path, sep=';')
    return data

st.set_page_config(layout='wide')

st.title('House Rocket - Imóveis para Comprar')
st.header('Base de Imóveis Completa')

# load data

data = get_data('house_rocket_tobuy.csv')
data = data[data['dormitory_type'] != 'check']
#data.drop('Unnamed: 0', axis=1, inplace=True)
st.dataframe(data.head(10))

# Números importantes
st.header('Números do negócio')
st.subheader('Total de Imóveis disponívels para compra')
st.subheader(data['price'].count())
st.subheader('Investimento Total')
st.subheader(data['price'].sum())
st.subheader('Receita Prevista 01')
st.write('Receita se optar por vender fora do segundo trimestre')
st.subheader(data['sale_price_01'].sum())
st.subheader('Receita Prevista 01')
st.write('Receita se optar por vender no segundo semestre')
st.subheader(data['sale_price_02'].sum())
st.subheader('Lucro Total na operação')
st.subheader(round(data['sale_price_02'].sum() - data['price'].sum(),2))
st.subheader('Margem de Lucro')
lucro_bruto = np.sum(data['sale_price_02']) - np.sum(data['price'])
st.subheader(round(lucro_bruto/data['sale_price_02'].sum(),2) * 100)

# Filtros
st.sidebar.title('Filtros de Atributo')
zipcode = st.sidebar.multiselect('Zipcode',
            data['zipcode'].unique())
min_v = int(data['price'].min())
max_v = int(data['price'].max())
avg_v = int(data['price'].mean())
price_slider = st.sidebar.slider('Preços',min_value=min_v, max_value=max_v, value=avg_v)
bath = st.sidebar.multiselect('Número de Banheiros', sorted(data['bathrooms'].unique()))
bedrooms = st.sidebar.multiselect('Número de Quartos', sorted(data['bedrooms'].unique()))
waterview = st.sidebar.multiselect('Vista para o Mar', sorted(data['waterfront'].unique()))

# base filtrada
df = data[(data['price'] < price_slider)]

# base filtrada
st.header('Base Filtrada')
st.write(df.head(20))

# Gráfico de Barras
st.header('Gráficos')
st.subheader('Quantidade de imóvel pelo tipo de dormitório')
ax1 = df[['dormitory_type', 'price']].groupby('dormitory_type').count().reset_index()
ax1.columns=['Tipo de Dormitório', 'Quantidade']
fig1 = px.bar(ax1, x='Tipo de Dormitório', y='Quantidade')
st.plotly_chart(fig1, use_container_width=True)

# Gráfico de barras 2
st.subheader('Preço médio pelo tipo de dormitório')
ax2 = df[['dormitory_type', 'price']].groupby('dormitory_type').mean().reset_index()
ax2.columns=['Tipo de Dormitório', 'Média']
fig2 = px.bar(ax2, x='Tipo de Dormitório', y='Média')
st.plotly_chart(fig2, use_container_width=True)