import streamlit as st
import numpy as np
import pandas as pd

def get_variable_info(num_variables):
    var_info = []
    for i in range(num_variables):
        var_name = st.text_input(f"Variable Name {i+1}")
        var_type = st.radio(f"Variable Type {i+1}", ('Integer', 'Float', 'Categorical', 'Date', 'Integer_2', 'Float_2'))
        var_info.append((var_name.strip(), var_type.strip()))
    return var_info

def get_bounds_and_categories(var_info):
    bounds_info = {}
    categories_info = {}
    for i, (var_name, var_type) in enumerate(var_info):
        if var_type.lower() == 'integer':
            lower = st.number_input(f"Lower Bound for {var_name}", key=f"lower_{i}")
            upper = st.number_input(f"Upper Bound for {var_name}", key=f"upper_{i}")
            bounds_info[var_name] = (lower, upper)
        elif var_type.lower() == 'float':
            lower = st.number_input(f"Lower Bound for {var_name}", key=f"lower_{i}")
            upper = st.number_input(f"Upper Bound for {var_name}", key=f"upper_{i}")
            bounds_info[var_name] = (lower, upper)
        elif var_type.lower() == 'integer_2':
            mean = st.number_input(f"Mean for {var_name}", key=f"mean_{i}")
            std = st.number_input(f"Standard Deviation for {var_name}", key=f"std_{i}")
            bounds_info[var_name] = (mean, std)
        elif var_type.lower() == 'float_2':
            mean = st.number_input(f"Mean for {var_name}", key=f"mean_{i}")
            std = st.number_input(f"Standard Deviation for {var_name}", key=f"std_{i}")
            bounds_info[var_name] = (mean, std)
        elif var_type.lower() == 'categorical':
            categories_str = st.text_input(f"Unique Categories for {var_name} (comma separated)", key=f"cat_{i}")
            categories = [cat.strip() for cat in categories_str.split(',')]
            categories_info[var_name] = categories
        elif var_type.lower() == 'date':
            start_date = st.date_input(f"Start Date for {var_name}", key=f"start_date_{i}", 
                                       min_value=pd.to_datetime('1960-01-01'), max_value=pd.to_datetime('2024-12-31'),
                                       value=pd.to_datetime('1960-01-01'))
            end_date = st.date_input(f"End Date for {var_name}", key=f"end_date_{i}",
                                     min_value=pd.to_datetime('2024-01-01'), max_value=pd.to_datetime('2030-12-31'),
                                     value=pd.to_datetime('2024-01-01'))
            bounds_info[var_name] = (start_date, end_date)
    return bounds_info, categories_info

def datasetGenerator(sampleNo, var_info, bounds_info={}, categories_info={}):
    df_dict = {}

    for var_name, var_type in var_info:
        if var_type.lower() == 'integer':
            lower, upper = bounds_info.get(var_name, (0, 100))
            df_dict[var_name] = np.random.randint(lower, upper+1, size=sampleNo)
        elif var_type.lower() == 'float':
            lower, upper = bounds_info.get(var_name, (0.0, 100.0))
            df_dict[var_name] = np.random.uniform(lower, upper, size=sampleNo)
        elif var_type.lower() == 'integer_2':
            mean, std = bounds_info.get(var_name, (0, 1))
            df_dict[var_name] = np.random.normal(mean, std, size=sampleNo).astype(int)
        elif var_type.lower() == 'float_2':
            mean, std = bounds_info.get(var_name, (0.0, 1.0))
            df_dict[var_name] = np.random.normal(mean, std, size=sampleNo)
        elif var_type.lower() == 'categorical':
            categories = categories_info.get(var_name, ['cat1', 'cat2'])
            df_dict[var_name] = np.random.choice(categories, size=sampleNo)
        elif var_type.lower() == 'date':
            start_date, end_date = bounds_info.get(var_name, (pd.to_datetime('1960-01-01'), pd.to_datetime('2022-12-31')))
            df_dict[var_name] = np.random.choice(pd.date_range(start=start_date, end=end_date, freq='D'), size=sampleNo)

    df = pd.DataFrame(df_dict)
    return df

# Testing the code
num_variables = st.number_input("Number of Variables", min_value=1, max_value=10, value=3)
var_info = get_variable_info(num_variables)
bounds_info, categories_info = get_bounds_and_categories(var_info)
sampleNo = 100  # You can change this to the desired sample size
df = datasetGenerator(sampleNo, var_info, bounds_info, categories_info)

# Display the generated dataset
st.dataframe(df)

# Add a button to download the dataset as a CSV file
if st.button("Download CSV"):
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()  # Encode CSV data to base64
    href = f'<a href="data:file/csv;base64,{b64}" download="generated_dataset.csv">Download CSV File</a>'
    st.markdown(href, unsafe_allow_html=True)
