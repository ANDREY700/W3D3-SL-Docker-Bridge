
# ELBRUSE Bootcamp 
# 23-12-2024
# Home Work Week 3 Day 2
# Andrey Abramov
# abramov.andre@yandex.ru

# Page 02 of Streamlit project



import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title(f'{st.session_state.ticker_name}: Цена при открытии торгов')

plot = plt.figure(figsize=(5, 5), dpi=50)
plt.plot(st.session_state.historical_data.Close, 
         label=f'{st.session_state.ticker_name} Цена открытия', linewidth=2)
plt.title(f'{st.session_state.ticker_name} Цены открытия во времени')
plt.xlabel('Дата')
plt.ylabel('Цена при открытии торгов (USD)')
plt.legend()
plt.xticks(rotation=90)
plt.show()
st.pyplot(plot.get_figure())

if st.button('Скачать график'):
    plot.savefig("plot01.png")