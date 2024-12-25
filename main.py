# ELBRUSE Bootcamp 
# 23-12-2024
# Home Work Week 3 Day 2
# Andrey Abramov
# abramov.andre@yandex.ru

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import yfinance as yf
import functools

#initialization ----------------------------
if 'ticker_loaded' not in st.session_state:
    st.session_state['ticker_loaded'] = False
else:
    st.session_state.ticker_loaded = st.session_state.get('ticker_loaded', False)

if 'ticker_name' not in st.session_state:
    st.session_state['ticker_name'] = 'AAPL'


#Основная страница работы ----------------------------

# навигация по страницам
page01 = st.Page("page_01.py", title = 'Набор данных')
page011 = st.Page("page_04.py", title = 'Описание набора данных')
page02 = st.Page("page_02.py", title = 'Цена при открытии торгов')
page03 = st.Page("page_03.py", title = 'Ежедневная выручка')
page05 = st.Page("page_05.py", title = 'Среднее за 7 дней')
page06 = st.Page("page_06.py", title = 'Объем торгов')
page07 = st.Page("page_07.py", title = 'Матрица корреляции')


pg = st.navigation([page01, page011, page02, page03, page05, page06, page07])
pg.run()



def change_vis():
        st.session_state.ticker_loaded = not st.session_state.get('ticker_loaded', False)

# Add an items to the sidebar:
# выбор наиманования тикера

st.session_state.ticker_name = st.sidebar.selectbox(
    'Выберите тикер эмитента: ',
    ('AAPL', 'GOOGL', 'META', 'NFLX', 'AMZN'),
    on_change= change_vis
)

@functools.lru_cache(maxsize=10)
def load_data(ticker_name):
     return  yf.Ticker(st.session_state.ticker_name)


if st.sidebar.button("Загрузить данные по тикеру"):
    if 'ticker_name' not in st.session_state:
        st.session_state['ticker_name'] = 'AAPL'
    #st.write("Why hello there: " + ticker_name)
    st.session_state.ticker_data = load_data(st.session_state.ticker_name)
    # data for the last month
    st.session_state.historical_data = st.session_state.ticker_data.history(period="1mo")  
    #ticker_loaded = True
    st.session_state.ticker_loaded = True






