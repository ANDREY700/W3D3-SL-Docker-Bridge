
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

st.title(f'{st.session_state.ticker_name}: Распределение ежедневной выручки')


a10 = st.session_state.historical_data.copy().reset_index()
a10['AdjClose'] = a10.Close.pct_change(1)

import seaborn as sns
sns.set(style="whitegrid")
plot = plt.figure(figsize=(5, 5), dpi=50)
sns.histplot(a10['AdjClose'].pct_change().dropna(), bins=30, kde=True, color='blue')
plt.title(f'Распределение {st.session_state.ticker_name} Ежедневного изменения')
plt.xlabel('Ежедневное изменение')
plt.ylabel('Частота')
plt.show()
st.pyplot(plot.get_figure())

if st.button('Скачать график'):
    plot.savefig("plot01.png")