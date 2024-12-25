
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

st.title(f'{st.session_state.ticker_name}: Объем торгов по количеству акций')

a2 = st.session_state.historical_data.copy()
a2 = a2.reset_index()
#a2.columns = a2.columns.droplevel(-1)

plot = plt.figure(figsize=(5, 5), dpi=50)
plt.bar(a2.Date, a2['Volume'], color='green', alpha=0.7)
plt.title(f'{st.session_state.ticker_name} Объем торгов во времени')
plt.xlabel('Дата')
plt.xticks(rotation=90)
plt.ylabel('Объемм торгов')
plt.show()

st.pyplot(plot.get_figure())

if st.button('Скачать график'):
    plot.savefig("plot01.png")