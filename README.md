# Natural Language to SQL Query Converter App

## Overview

This web application allows users to convert natural language queries into SQL commands and execute them on a SQLite database. The app utilizes Google Generative AI to convert the queries and SQLite as the database engine for execution.

## Features

- Convert natural language queries to SQL commands.
- Execute SQL commands on a SQLite database.
- Display the results of the executed SQL commands.

## How it Works

1. **Upload SQLite Database File**
    - Upload your SQLite database file using the sidebar.
  
2. **Provide Google API Key**
    - Enter your Google API key in the provided text box on the sidebar.

3. **Enter Natural Language Query**
    - Write your natural language query in the text area provided.

4. **Execute Query**
    - Click the "Execute Query" button to convert the natural language query to an SQL command and execute it on the SQLite database.
  
5. **View Results**
    - Once the query is executed, the results will be displayed below along with the executed SQL command.

## Setup Instructions

### Prerequisites

- Python 3.x
- Git

### Installation Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/adikul25/langchain-googleGenAI-SQL.git
    ```

2. **Navigate to the Project Directory**

3. **Install Required Packages**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the App**

    ```bash
    streamlit run app.py
    ```

### Configuration

- **API Key**: Obtain a Google API key from the [Google Cloud Console](https://console.cloud.google.com/).
- **SQLite Database**: Prepare your SQLite database file (.db) to upload.

### Usage

1. **Upload Database and API Key**
    - Upload your SQLite database file and provide your Google API key in the respective fields on the sidebar.

2. **Enter Query**
    - Write your natural language query in the text area provided.

3. **Execute Query**
    - Click the "Execute Query" button to execute the query and view the results.

## Disclaimer

- Not all converted SQL commands may be accurate or suitable for execution.
- Always review and verify the converted SQL command before executing it on your database.

For any queries or feedback, please contact adikulkarni25@gmail.com.
