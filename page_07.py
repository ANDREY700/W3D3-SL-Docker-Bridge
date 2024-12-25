
# ELBRUSE Bootcamp 
# 23-12-2024
# Home Work Week 3 Day 2
# Andrey Abramov
# abramov.andre@yandex.ru

# Page 03 of Streamlit project



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go

st.title(f'{st.session_state.ticker_name}: Матрица корреляции')


correlation_matrix = st.session_state.historical_data[['Open', 'High', 'Low', 'Close', 'Volume']].corr()

plot = plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title(f'Тепловая карта корреляции по тикеру {st.session_state.ticker_name}')
plt.show()
st.pyplot(plot.get_figure())

if st.button('Скачать график'):
    plot.savefig("plot01.png")

st.text(f"Матрица корреляции в цифрах {st.session_state.ticker_name} за прошедший год:")
st.table(correlation_matrix)