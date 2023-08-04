import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

from vega_datasets import data

source = pd.read_csv

brush = alt.selection_interval(resolve='global')

base = alt.Chart(source).mark_point().encode(
    y='Miles_per_Gallon',
    color=alt.condition(brush, 'Origin', alt.ColorValue('gray')),
).add_params(
    brush
).properties(
    width=250,
    height=250
)

c = base.encode(x='Horsepower') | base.encode(x='Acceleration')

st.altair_chart(c, use_container_width=True)
