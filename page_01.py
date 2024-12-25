
# ELBRUSE Bootcamp 
# 23-12-2024
# Home Work Week 3 Day 2
# Andrey Abramov
# abramov.andre@yandex.ru

# Page 01 of Streamlit project

import streamlit as st



#st.title('Страница 01')

if st.session_state.ticker_loaded:    
    st.title(f'{st.session_state.ticker_name}: Данные загружены')
    st.text(f"Исторические данные по тикеру {st.session_state.ticker_name} за последний месяц:")
    st.table(st.session_state.historical_data[['Open', 'High', 'Low', 'Close', 'Volume']])
else:
    st.title('Данные по тикеру еще не загружены')
    st.write('Выберите наименование тикера слева и нажмите "Загрузить данные".') 

