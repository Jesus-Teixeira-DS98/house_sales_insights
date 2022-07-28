import pandas as pd
import streamlit as st
import numpy as np
from plotly import express as px
from datetime import datetime

# ------------------------------------------
# settings
# ------------------------------------------
st.set_page_config(layout='wide')
pd.set_option('display.float_format', lambda x: '%.2f' % x)
@st.cache( allow_output_mutation=True )

# ------------------------------------------
# Helper Functions
# ------------------------------------------

def get_data(path):
    data = pd.read_csv(path, sep=';')
    return data

# Transforming

def transformacoes(data):
    st.title('House Rocket - Imóveis para Comprar')
    st.write('Ferramenta para Analisar Características dos imóveis e tomar decisões de compra e venda.')
    st.header('Base de Imóveis Completa')
    dataset = data[data['dormitory_type'] != 'check']
    dataset.drop('Unnamed: 0', axis=1,inplace=True)
    st.dataframe(dataset.head(10))
    # Números importantes
    st.header('Números do negócio')
    st.subheader('Total de Imóveis disponívels para compra:')
    st.subheader(dataset['price'].count())
    st.subheader('Investimento Total:')
    st.subheader(dataset['price'].sum())
    st.subheader('Receita Prevista 01:')
    st.write('Receita se optar por vender fora do segundo trimestre')
    st.subheader(dataset['sale_price_01'].sum())
    st.subheader('Receita Prevista 02:')
    st.write('Receita se optar por vender no segundo semestre')
    st.subheader(dataset['sale_price_02'].sum())
    st.subheader('Lucro Total na operação:')
    st.subheader(round(dataset['sale_price_02'].sum() - dataset['price'].sum(),2))
    st.subheader('Margem de Lucro:')
    lucro_bruto = np.sum(dataset['sale_price_02']) - np.sum(dataset['price'])
    st.subheader(round(lucro_bruto/dataset['sale_price_02'].sum(),2) * 100)
    return dataset

def filtros(data):
    # Filtros
    st.sidebar.title('Filtros de Atributo')
    zipcode = st.sidebar.multiselect('Zipcode',
                data['zipcode'].unique())
    min_v = int(data['price'].min())
    max_v = int(data['price'].max())
    avg_v = int(data['price'].mean())
    price_slider = st.sidebar.slider('Preços',min_value=min_v, max_value=max_v, value=avg_v)
    min_m2 = int(data['m2_living'].min())
    max_m2 = int(data['m2_living'].max())
    avg_m2 = int(data['m2_living'].mean())
    area_slider = st.sidebar.slider("Metro Quadrado",min_value=min_m2, max_value=max_m2, value=avg_m2 )
    bath = st.sidebar.multiselect('Número de Banheiros', sorted(data['bathrooms'].unique()))
    bedrooms = st.sidebar.multiselect('Número de Quartos', sorted(data['bedrooms'].unique()))
    waterview = st.sidebar.multiselect('Vista para o Mar', sorted(data['waterfront'].unique()))

    # base filtrada
    df = data[(data['price'] <= price_slider)]
    df1 = df.copy()
    df2 = df1[df1['m2_living'] <= area_slider]
    df3 = df2.copy()
    if zipcode == []:
        df4 = df3.copy()
    else:
        df4 = df3.loc[data['zipcode'].isin(zipcode), :]
    if bath == []:
        df5 = df4.copy()
    else:
        df5 = df4.loc[df4['bathrooms'].isin(bath), :]
    if bedrooms == []:
        df6 = df5.copy()
    else:
        df6 = df5.loc[df5['bedrooms'].isin(bedrooms), :]
    if waterview == []:
        df7 = df6.copy()
    else:
        df7 = df6.loc[df6['waterfront'].isin(waterview), :]
    # base filtrada
    st.header('Base Filtrada')
    st.write(df7.head(20))
    return df7

def graficos(df7):
    # Gráfico de Barras
    st.header('Gráficos')
    st.subheader('Quantidade de imóvel pelo tipo de dormitório')
    ax1 = df7[['dormitory_type', 'price']].groupby('dormitory_type').count().reset_index()
    ax1.columns=['Tipo de Dormitório', 'Quantidade']
    fig1 = px.bar(ax1, x='Tipo de Dormitório', y='Quantidade')
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfico de barras 2
    st.subheader('Preço médio pelo tipo de dormitório')
    ax2 = df7[['dormitory_type', 'price']].groupby('dormitory_type').mean().reset_index()
    ax2.columns=['Tipo de Dormitório', 'Média']
    fig2 = px.bar(ax2, x='Tipo de Dormitório', y='Média')
    st.plotly_chart(fig2, use_container_width=True)

    # Gráfico de linha
    st.subheader('Variação do preço mediano')
    ax3 = df7[['price', 'date']].groupby('date').median().reset_index()
    ax3.columns=['price', 'date']
    fig3 = px.line(ax3, x='price', y='date')
    st.plotly_chart(fig3, use_container_width=True)

    # Mapa
    st.subheader('Distribuição de imóveis pela cidade')
    houses = df7[['id', 'price', 'lat', 'long', 'level']]
    fig4 = px.scatter_mapbox(houses, lat='lat', lon='long',color_continuous_scale='px.colors.cyclical.IceFire',
                             size='price',size_max=15,zoom=10,color='level')
    fig4.update_layout(mapbox_style="open-street-map")
    fig4.update_layout(height=600, margin={"r":0,"t":0,"l":0,"b":0})
    st.plotly_chart(fig4, use_container_width=True)

    return None

if __name__ == "__main__":
    path = 'house_rocket_tobuy.csv'
    data = get_data( path )
    dataset = transformacoes(data)
    df7 = filtros(dataset)
    graficos(df7)

