import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="My Awesome App",  # Title that appears on the browser tab
    page_icon="🚀",              # Emoji or image as the favicon
    layout="wide",               # Optional: Layout of the app ("centered" or "wide")
    initial_sidebar_state="collapsed"  # Optional: Default state of the sidebar
)


# Create a custom component
def my_custom_component(name: str):
    html_content = f"""
    <div style="border: 2px solid #4CAF50; padding: 20px; text-align: center;">
        <h2>Hello, {name}!</h2>
    </div>
    """
    return components.html(html_content, height=100)

# Streamlit app
st.title("Custom Component Example")
user_name = st.text_input("Enter your name:")
if user_name:
    my_custom_component(user_name)

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.title("Welcome to the Home Page!")
elif page == "About":
    st.title("About Us")
    st.write("This is the about page.")
elif page == "Contact":
    st.title("Contact Us")
    st.write("Reach us at contact@example.com")
