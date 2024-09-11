import streamlit as st

# Create a title    
st.title("Streamlit Test")

# Create a text input box
text_input = st.text_input("Enter some text:")

# Create a submit button
if st.button("Submit"):
    st.write("You've inputted:", text_input)

# change background to light blue
st.markdown(
    """
    <style>
    .reportview-container {
        background: lightblue
    }
    </style>
    """,
    unsafe_allow_html=True
)