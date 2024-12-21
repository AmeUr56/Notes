import streamlit as st
from datetime import datetime

#------------------------Hide Hamburger Menu & Footer-----------------------#
# Set page configuration
st.set_page_config(page_title="My App", layout="wide", initial_sidebar_state="collapsed")

# Custom CSS to hide hamburger menu and footer
hide_streamlit_style = """
    <style>
        /* Hide the hamburger menu */
        .css-1d391kg {display: none;}
        /* Hide Streamlit footer */
        footer {visibility: hidden;}
    </style>
"""

# Inject custom CSS
st.markdown(hide_streamlit_style, unsafe_allow_html=True)
#---------------------------------------------------------------------------#

# Single-line text input
st.title("Single-line Text Input")
name = st.text_input("Enter your name")
st.write("Hello, ", name)

# Multi-line text input
st.title("Multi-line Text Input")
message = st.text_area("Enter your message", "Type here...")
st.write("Your message:", message)

# Numeric input
st.title("Numeric Input")
age = st.number_input("Enter your age", min_value=0, max_value=100, value=25)
st.write("Your age:", age)

# Date input
st.title("Date Input")
birth_date = st.date_input("Enter your birth date")
st.write("Your birth date:", birth_date)

# Time input
st.title("Time input")
appointment_time = st.time_input("Set your appointment time",value=datetime.now())
st.write("Appointment time:", appointment_time)

# File uploader
st.title("File Upload")
uploaded_file = st.file_uploader("Choose a file", type=["jpg", "png"])
if uploaded_file is not None:
    st.image(uploaded_file)

# Dropdown selection (single choice)
st.title("Single-choice Dropdown")
color = st.selectbox("Choose your favorite color", ["Red", "Green", "Blue"])
st.write("Your favorite color is:", color)

# Multi-dropdown selection (multiple choices)
st.title("Multiple-choice Dropdown")
fruits = st.multiselect("Select your favorite fruits", ["Apple", "Banana", "Orange", "Mango"])
st.write("Your selected fruits:", fruits)

# Radio buttons
st.title("Radio buttons")
feedback = st.radio("How do you rate our service?", ["Excellent", "Good", "Average", "Poor"])
st.write("Your feedback:", feedback)

# Slider input
st.title("Slider Input")
rating = st.slider("Rate our app", 0, 10, 5)
st.write("Your rating:", rating)

# Checkbox input
st.title("Checkbox Input")
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.write("You have agreed.")
else:
    st.write("You have not agreed.")

# Button input
st.title("Button")
if st.button("Click me"):
    st.write("Button clicked!")

# Form input
st.title("Form")
with st.form(key="my_form"):
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age",min_value=0,max_value=200)
    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write(f"Hello {name}, ur age is {age}")
