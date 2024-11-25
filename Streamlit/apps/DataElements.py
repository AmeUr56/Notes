import streamlit as st
import pandas as pd

# Sample DataFrame
data = {
    'Name': ['John', 'Alice', 'Bob', 'Mary'],
    'Age': [25, 30, 22, 28],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Miami']
}
df = pd.DataFrame(data)

st.title("DataFrame(interactive table)")
# Display DataFrame
st.dataframe(df)

st.title("Static Table")
st.table(df)

# Sample JSON data
json_data = {
    "name": "John",
    "age": 25,
    "city": "New York"
}

st.title("Json")
# Display JSON data
st.json(json_data)
