import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar os dados processados
def carregar_dados():
    file_path = "Relatorio_Consolidado.xlsx"
    df = pd.read_excel(file_path, sheet_name="Resumo Consolidado")
    df['ANO_MES'] = df['ANO_MES'].astype(str)
    return df

df = carregar_dados()

# Configuração da página
st.set_page_config(page_title='Dashboard de Vendas', layout='wide')

# Título
st.title("📊 Dashboard de Performance de Vendas")

# Criar filtros
col1, col2, col3 = st.columns(3)

with col1:
    empreendimento = st.multiselect("Selecione o Empreendimento:", options=df['EMPREENDIMENTO'].unique(), default=df['EMPREENDIMENTO'].unique())
with col2:
    ano = st.multiselect("Selecione o Ano:", options=df['ANO_MES'].str[:4].unique(), default=df['ANO_MES'].str[:4].unique())
with col3:
    mes = st.multiselect("Selecione o Mês:", options=df['ANO_MES'].str[-2:].unique(), default=df['ANO_MES'].str[-2:].unique())

# Filtrando os dados
df_filtrado = df[(df['EMPREENDIMENTO'].isin(empreendimento)) & (df['ANO_MES'].str[:4].isin(ano)) & (df['ANO_MES'].str[-2:].isin(mes))]

# Gráfico de evolução das taxas de conversão
grafico_taxas = px.line(df_filtrado, x='ANO_MES', y=['taxa_pastas_completas', 'taxa_pastas_aprovadas', 'taxa_vendas'],
                         labels={'value': 'Taxa (%)', 'ANO_MES': 'Ano-Mês'}, title="Evolução das Taxas de Conversão",
                         markers=True)
st.plotly_chart(grafico_taxas, use_container_width=True)

# Gráfico de vendas mensais
grafico_vendas = px.bar(df_filtrado, x='ANO_MES', y=['vendas_unidades', 'vendas_valor'],
                        labels={'value': 'Total', 'ANO_MES': 'Ano-Mês'}, title="Vendas Mensais - Quantidade e Valor",
                        barmode='group')
st.plotly_chart(grafico_vendas, use_container_width=True)

# Exibir tabela de dados
st.subheader("📋 Dados Detalhados")
st.dataframe(df_filtrado)

import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados():
    url = "https://github.com/JEANGFS88/DASHVENDASDOMMUS/blob/master/Relatorio_Consolidado.xlsx"
    df = pd.read_excel(url, sheet_name="Resumo Consolidado", engine="openpyxl")
    df['ANO_MES'] = df['ANO_MES'].astype(str)
    return df

df = carregar_dados()

uploaded_file = st.file_uploader("Envie o arquivo Excel", type=["xlsx"])

if uploaded_file is not None:
    df = pd.read_excel(uploaded_file, sheet_name="Resumo Consolidado", engine="openpyxl")
    st.write(df)

import pandas as pd
import streamlit as st

@st.cache_data
def carregar_dados():
    url = "https://github.com/JEANGFS88/DASHVENDASDOMMUS/blob/master/Relatorio_Consolidado.xlsx"
    df = pd.read_excel(url, sheet_name="Resumo Consolidado", engine="openpyxl")
    df['ANO_MES'] = df['ANO_MES'].astype(str)
    return df

df = carregar_dados()

