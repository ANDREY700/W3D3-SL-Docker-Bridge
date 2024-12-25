
# ELBRUSE Bootcamp 
# 23-12-2024
# Home Work Week 3 Day 2
# Andrey Abramov
# abramov.andre@yandex.ru

# Page 04 of Streamlit project



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = st.session_state.historical_data.copy()

st.title(f'{st.session_state.ticker_name}: Описание набора данных')

st.subheader("Размер набора данных")

st.write('Количество строк:', df.shape[0])
st.write('Количество столбцов:', df.shape[1])

st.subheader("Объем занимаемой памяти, байт")
st.dataframe(df.memory_usage() ) #
st.write('Объем занимаемой памяти по всему набору ', 
         df.memory_usage().sum(), ' байт')

st.subheader("Перечень столбцов")
st.dataframe(df.columns.to_list())

st.subheader("Типы данных столбцов набора данных")
st.write(pd.DataFrame(df.dtypes.astype('str'), columns=['тип данных']))

st.subheader("Описательная статистика по столбцам")
st.dataframe(df.describe())

st.subheader("Пропущенные значения")
st.write(pd.DataFrame(df.isnull().sum().sort_values(ascending=False), 
                      columns=['Число пропущенных значений']))

