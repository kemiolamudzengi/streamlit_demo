import streamlit as st
import pandas as pd
import numpy as np
import altair as alt


source = pd.read_csv('cars_data.csv')

brush = alt.selection_interval(resolve='global')

base = alt.Chart(source).mark_point().encode(
    y='mileage',
    color=alt.condition(brush, 'country', alt.ColorValue('gray')),
).add_params(
    brush
).properties(
    width=250,
    height=250
)

c = base.encode(x='hp') | base.encode(x='acceleration')

st.altair_chart(c, use_container_width=True)
