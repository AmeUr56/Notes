import streamlit as st

# Title
st.title("Streamlit Text Functions Demo")

# Header
st.header("1. Header: This is a Section Heading")

# Subheader
st.subheader("2. Subheader: This is a Subsection Heading")

# Plain Text
st.text("3. Text: This is plain, unformatted text.")

# Markdown
st.markdown("""
4. Markdown: This text is **bold**, _italic_, and supports:
- Bullet lists
- [Links](https://streamlit.io)
""")

# Write
st.write("5. Write: This is a versatile method for displaying various elements.")
st.write("It supports **Markdown**, _text_, and even **Python objects** like dataframes!")

# Caption
st.caption("6. Caption: This is small-sized text, useful for annotations.")

# Code
st.code("""
# Python Code Example
def greet(name):
    return f"Hello, {name}!"
""", language="python")

# LaTeX
st.latex(r"8. LaTeX: E = mc^2")

# Success Message
st.success("9. Success: Task completed successfully!")

# Warning Message
st.warning("10. Warning: Be cautious!")

# Error Message
st.error("11. Error: Something went wrong!")

# Informational Message
st.info("12. Info: Here's some additional information.")

# Defining a metric value and its delta
current_temperature = 72
temperature_delta = 2  # This could be a change in temperature from the previous value

# Using st.metric to display the current temperature and its delta
st.metric(label="13. Current Temperature", value=f"{current_temperature}°F", delta=f"{temperature_delta}°F")

# You can also style it with color
st.metric(label="Temperature Change", value=f"{temperature_delta}°F", delta_color="inverse")

# Balloons
st.write("14. Balloons: Click the button below to celebrate!")
if st.button("Celebrate!"):
    st.balloons()
