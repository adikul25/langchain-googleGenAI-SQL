import streamlit as st
import os
from src.SQLAgent import DatabaseQueryExecutor
from src.db_run import DatabaseExecutor
import pandas as pd

# Set page layout
st.set_page_config(layout="wide", page_title="Database Query Executor App", page_icon=":bar_chart:")

# Title and description
st.title("Natural Language to SQL Query Converter")
# st.markdown("""
#     This app enables you to convert natural language queries into SQL commands and execute them on a SQLite database.
# """)

# Sidebar
st.sidebar.title("Navigation")
navigation = st.sidebar.radio("Go to", ["Execute Query", "About"])

# About tab content
if navigation == "About":
        st.markdown("""
    ### About
    
    This web app enables you to execute SQL queries on a SQLite database by converting natural language queries to SQL commands using Google Generative AI. Simply upload your SQLite database file, provide your Google API key, and write your natural language query to get started.
    
    **How it Works:**
    - The app uses Google Generative AI to convert your natural language query into an SQL command.
    - The converted SQL command is then executed on the SQLite database you've uploaded.
    
    **Instructions:**
    1. Upload your SQLite database file using the sidebar.
    2. Enter your Google API key in the provided text box.
    3. Write your natural language query in the text area.
    4. Click the "Execute Query" button to see the results.
    
    **Disclaimer:**
    - Not all converted SQL commands may be accurate or suitable for execution.
    - Always review and verify the converted SQL command before executing it on your database.
    
    For any queries or feedback, please contact support@example.com.
    """)
else:
    # Query execution tab content
    
    # Sidebar settings
    st.sidebar.title("Settings")
    #show_api_key = st.sidebar.checkbox("Show API Key")
    api_key = st.sidebar.text_input("Enter your Google API Key:", "", type="password")
    uploaded_file = st.sidebar.file_uploader("Upload SQLite database file", type="db")

    # Database and API key validation
    if api_key and uploaded_file:
        # Save the uploaded file to a temporary location
        with open(f"temp.db", "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        # Initialize DatabaseQueryExecutor with API key and database URI
        db_uri = f"sqlite:///temp.db"
        db_executor = DatabaseExecutor('temp.db')
        df_result = db_executor.db_execute_query("SELECT * FROM sqlite_master WHERE type='table'")
        sql_statements = df_result['sql'].tolist()

        # Display tables in an expander
        with st.expander("Database Tables"):
            for sql in sql_statements:
                st.code(sql, language='sql')

        executor = DatabaseQueryExecutor(api_key, db_uri)
        
        # Query input
        query = st.text_area("Enter your SQL query:", "", height=10)
        
        # Execute query and display result
        if st.button("Execute Query"):
            if query:
                try:
                    sql_command = executor.execute_query(query)
                    st.subheader("Executed SQL Command:")
                    df = db_executor.db_execute_query(sql_command)
                    
                    # Limit rows displayed in dataframe
                    st.dataframe(df.head(50))
                    
                    # Display SQL query in an expander
                    with st.expander('SQL Query'):
                        st.code(sql_command, language='sql')
                    
                    st.success("Query executed successfully!")
                except Exception as e:
                    st.error(f"Error executing SQL query: {e}")
            else:
                st.warning("Please enter an SQL query.")
        

    else:
        st.warning("Please provide both API key and SQLite database file.")



