import streamlit as st

def explain_data_types():
    st.sidebar.title("Data Types Explanation")
    st.sidebar.markdown("**Integer:** Whole numbers without decimals.")
    st.sidebar.markdown("**Float:** Numbers with decimals.")
    st.sidebar.markdown("**Integer_2:** Integers generated based on mean and standard deviation.")
    st.sidebar.markdown("**Float_2:** Floats generated based on mean and standard deviation.")
    st.sidebar.markdown("**Categorical:** Variables that can take on one of a limited, and usually fixed, number of possible values.")
