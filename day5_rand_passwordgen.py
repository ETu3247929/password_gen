import random
import streamlit as st


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator(nr_letters, nr_symbols, nr_numbers):
    password = []
    for _ in range(nr_letters):
        password.append(random.choice(letters))
    for _ in range(nr_symbols):
        password.append(random.choice(symbols))
    for _ in range(nr_numbers):
        password.append(random.choice(numbers))
    random.shuffle(password)
    return ''.join(password)

st.title("Welcome to the PyPassword Generator!")

nr_letters = st.number_input("How many letters would you like in your password?", min_value=0, value=0, step=1)
nr_symbols = st.number_input("How many symbols would you like?", min_value=0, value=0, step=1)
nr_numbers = st.number_input("How many numbers would you like?", min_value=0, value=0, step=1)

if st.button('Generate Password'):
    if nr_letters + nr_symbols + nr_numbers > 0:
        st.text(password_generator(nr_letters, nr_symbols, nr_numbers))
    else:
        st.error("You must have at least one character in your password.")
