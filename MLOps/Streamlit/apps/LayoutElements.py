import streamlit as st
import time

st.toast("Welcome Here!")

# Adding widgets to the sidebar
st.sidebar.title("Sidebar Example")
if st.sidebar.button("Click Me"):
    # Using a spinner
    with st.spinner("Loading..."):
        time.sleep(5)
    
    st.sidebar.error("Why did you click!!!!!")
    
st.sidebar.slider("Adjust Value", 0, 100, 50)

# Grouping elements in a container
with st.container():
    st.title("Container Title")
    st.write("This is inside a container.")
    st.button("Container Button")
    
st.write("This is outside the container.")

# Creating a 3-column layout
col1, col2, col3 = st.columns(3)

st.title("3-Column layout")
col1.write("Column 1")
col1.code("#This is Python comment\nprint('Hello World')")
col2.button("Button in Column 2")
col3.metric("Metric", "50%", "+5%")

st.title("Expandable section")
# Expandable section
with st.expander("See More"):
    st.write("Hidden content revealed when expanded!")

st.title("Empty section")
# Placeholder for dynamic content
placeholder = st.empty()

# Update the placeholder
import time
for i in range(2):
    placeholder.write(f"Updating... {i}")
    time.sleep(1)

placeholder.write("Done!")

st.title("Progress bar")
# Displaying a progress bar
progress = st.progress(0)
for i in range(100):
    time.sleep(0.05)
    progress.progress(i + 1)

# Creating tabs
st.write("Tabs Section")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])

with tab1:
    st.write("Content in Tab 1")

with tab2:
    st.write("Content in Tab 2")
