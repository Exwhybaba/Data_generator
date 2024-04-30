import streamlit as st
import numpy as np
import pandas as pd
import base64

def get_variable_info(num_variables):
    var_info = []
    for i in range(num_variables):
        var_name = st.text_input(f"Variable Name {i+1}_{np.random.randint(100)}")
        var_type = st.radio(f"Variable Type {i+1}_{np.random.randint(100)}", ('Integer', 'Float', 'Categorical', 'Date', 'Integer_2', 'Float_2'))
        var_info.append((var_name.strip(), var_type.strip()))
    return var_info

def get_bounds_and_categories(var_info):
    bounds_info = {}
    categories_info = {}
    for i, (var_name, var_type) in enumerate(var_info):
        if var_type.lower() == 'integer':
            lower = st.number_input(f"Lower Bound for {var_name}", key=f"lower_{i}_{np.random.randint(100)}")
            upper = st.number_input(f"Upper Bound for {var_name}", key=f"upper_{i}_{np.random.randint(100)}")
            bounds_info[var_name] = (lower, upper)
        elif var_type.lower() == 'float':
            lower = st.number_input(f"Lower Bound for {var_name}", key=f"lower_{i}_{np.random.randint(100)}")
            upper = st.number_input(f"Upper Bound for {var_name}", key=f"upper_{i}_{np.random.randint(100)}")
            bounds_info[var_name] = (lower, upper)
        elif var_type.lower() == 'integer_2':
            mean = st.number_input(f"Mean for {var_name}", key=f"mean_{i}_{np.random.randint(100)}")
            std = st.number_input(f"Standard Deviation for {var_name}", key=f"std_{i}_{np.random.randint(100)}")
            bounds_info[var_name] = (mean, std)
        elif var_type.lower() == 'float_2':
            mean = st.number_input(f"Mean for {var_name}", key=f"mean_{i}_{np.random.randint(100)}")
            std = st.number_input(f"Standard Deviation for {var_name}", key=f"std_{i}_{np.random.randint(100)}")
            bounds_info[var_name] = (mean, std)
        elif var_type.lower() == 'categorical':
            categories_str = st.text_input(f"Unique Categories for {var_name} (comma separated)", key=f"cat_{i}_{np.random.randint(100)}")
            categories = [cat.strip() for cat in categories_str.split(',')]
            categories_info[var_name] = categories
        elif var_type.lower() == 'date':
            start_date = st.date_input(f"Start Date for {var_name}", key=f"start_date_{i}_{np.random.randint(100)}", 
                                       min_value=pd.to
