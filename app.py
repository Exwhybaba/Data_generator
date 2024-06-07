import streamlit as st
import pandas as pd
import base64
from dataset_generator import get_variable_info, get_bounds_and_categories, datasetGenerator
from dataInfo import explain_data_types

# Main app
def main(debug=True):
    st.title("Dataset Generator")

    # Get number of samples
    sampleNo = st.number_input('Number of Samples', min_value=1, step=1, value=100)

    # Get number of variables
    num_variables = st.number_input('Number of Variables', min_value=1, step=1, value=1)

    # Get variable information
    var_info = get_variable_info(num_variables)

    # Get bounds and categories information
    bounds_info, categories_info = get_bounds_and_categories(var_info)

    # Generate data and display DataFrame
    if st.button("Generate Dataset"):
        df = datasetGenerator(sampleNo, var_info, bounds_info, categories_info)
        st.dataframe(df)


    # Add download button
    if 'df' in locals() and df is not None:
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # Encoding to base64
        href = f'<a href="data:file/csv;base64,{b64}" download="generated_dataset.csv">Download CSV File</a>'
        st.markdown(href, unsafe_allow_html=True)

if __name__ == "__main__":
    main()

