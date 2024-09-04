import streamlit as st
import pandas as pd
import automaton_tool


st.markdown("""
    <style>
        .reportview-container {
            margin-top: -2em;
        }
        #MainMenu {visibility: hidden;}
        .stDeployButton {display:none;}
        footer {visibility: hidden;}
        #stDecoration {display:none;}
    </style>
""", unsafe_allow_html=True)
st.title("Upload and Process CSV Data")

# Create two columns for layout
col1, col2 = st.columns(2)

# Upload CSV file
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)

    # Limit the number of rows displayed to 30
    df_display = df.head(30)
    
    # Display the dataframe in the first column
    with col1:
        st.write("Uploaded Data (Showing up to 30 rows):")
        st.dataframe(df_display)
        
        # Provide an option to download the uploaded data as CSV
        csv_uploaded = df.to_csv(index=False)
        st.download_button(
            label="Download Uploaded CSV",
            data=csv_uploaded,
            file_name='uploaded_data.csv',
            mime='text/csv'
        )

    # Check if required columns exist
    if 'Data_Points' in df.columns and 'Deformation' in df.columns:
        st.success("Required columns found!")
        
        # Process Data and Plot
        new_df, fig = automaton_tool.process_and_plot(df)

        # Limit the number of rows in processed data to 30
        new_df_display = new_df.head(30)

        # Display the processed data in the second column
        with col2:
            st.write("Processed Data (Showing up to 30 rows):")
            st.write(new_df_display)
            
            # Provide an option to download the processed data as CSV
            csv_processed = new_df.to_csv(index=False)
            st.download_button(
                label="Download Processed CSV",
                data=csv_processed,
                file_name='processed_data.csv',
                mime='text/csv'
            )

        # Show the graph in Streamlit
        st.pyplot(fig)
    else:
        st.error("The CSV file does not contain the required columns: 'Data_Points' and 'Deformation'")
else:
    st.info("Please upload a CSV file.")
