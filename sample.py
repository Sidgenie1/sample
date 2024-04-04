import streamlit as st

# Title of the app
st.title('Streamlit Example App')

# Ask for user's name
name = st.text_input('What is your name?')

# Ask for a number
number = st.number_input('Enter a number', value=0)  # Default value is 0

# Create a button. When clicked, it will perform the operation below
if st.button('Greet Me!'):
    st.write(f'Hello, {name}!')  # Greeting the user

if st.button('Square the Number'):
    square = number ** 2  # Calculating the square of the number
    st.write(f'The square of {number} is {square}.')  # Displaying the result
