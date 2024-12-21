import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import matplotlib.pyplot as plt
import seaborn as sns;sns.set()
import plotly.express as px

# Sample data
data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['A', 'B', 'C']
)

st.title("Line Chart")
# Display line chart
st.line_chart(data)

st.title("Area Chart")
# Display area chart
st.area_chart(data)

st.title("Bar Chart")
# Display bar chart
st.bar_chart(data)


# Altair chart example
chart = alt.Chart(data.reset_index()).mark_line().encode(
    x='index',
    y='A'
)

st.title("Altair Chart")
# Display Altair chart
st.altair_chart(chart, use_container_width=True)


# Matplotlib example
fig, ax = plt.subplots()
ax.plot(data.index, data['A'], label='A')
ax.legend()

st.title("Matplotlib Chart")
# Display Matplotlib chart
st.pyplot(fig)


# Plotly example
fig = px.scatter(data, x='A', y='B', title="Scatter Plot")

st.title("Plotly Chart")
# Display Plotly chart
st.plotly_chart(fig)

# Vega-Lite example
vega_chart = {
    'mark': 'bar',
    'encoding': {
        'x': {'field': 'index', 'type': 'ordinal'},
        'y': {'field': 'A', 'type': 'quantitative'}
    },
    'data': {'values': data.reset_index().to_dict(orient='records')}
}

st.title("Vega-List Chart")
# Display Vega-Lite chart
st.vega_lite_chart(vega_chart, use_container_width=True)
