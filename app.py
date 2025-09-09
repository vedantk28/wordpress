import streamlit as st

st.set_page_config(page_title="Simple Calculator", layout="centered")

st.title("🔢 Simple Calculator")

# Input fields
num1 = st.number_input("Enter first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter second number", value=0.0, format="%.2f")

# Operation selection
operation = st.selectbox("Choose operation", ["Add", "Subtract", "Multiply", "Divide"])

# Calculate result
def calculate(n1, n2, op):
    if op == "Add":
        return n1 + n2
    elif op == "Subtract":
        return n1 - n2
    elif op == "Multiply":
        return n1 * n2
    elif op == "Divide":
        return "∞" if n2 == 0 else n1 / n2

if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    st.success(f"Result: {result}")
