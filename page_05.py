
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

st.title(f'{st.session_state.ticker_name}: Среднее за 7 дней')


a40 = st.session_state.historical_data.copy()
a40 = a40.reset_index()
a40['ave'] = a40['Close'].rolling(window=7).mean()

plot = plt.figure(figsize=(5, 5), dpi=50)
plt.plot(a40.Date, a40['Close'], '-g', label="Цена закрытия USD")
plt.plot(a40.Date, a40['ave'], ':r', label="Среднее за 7 дней")
plt.style.use('_mpl-gallery')
plt.title(f'{st.session_state.ticker_name} Среднее за 7 дней')
plt.xlabel("Дата")
plt.xticks(rotation=90)
plt.legend();
plt.show()

st.pyplot(plot.get_figure())

if st.button('Скачать график'):
    plot.savefig("plot01.png")

st.text(f"Матрица корреляции в цифрах {st.session_state.ticker_name} за прошедший год:")
st.table(a40[['Open', 'High', 'Low', 'Close', 'Volume', 'ave']])

