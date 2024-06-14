# Gemini SQL Data Retrieval App

This is a Streamlit application designed to retrieve data from a SQL database using natural language queries. The app leverages Google Generative AI for interpreting natural language input and converting it to SQL queries.

## Features

- **Natural Language Query Input**: Enter your queries in natural language.
- **SQL Execution**: Converts natural language to SQL queries and executes them on a SQLite database.
- **Results Display**: Displays the results of the SQL queries in the app.

## Project Structure

- `app.py`: The main Streamlit application script.
- `sql.py`: Contains helper functions for SQL query execution.
- `student.db`: The SQLite database used in the application.
- `requirements.txt`: Lists the Python dependencies for the project.

## Installation

To run this project locally

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/gemini-sql-data-retrieval-app.git
    cd gemini-sql-data-retrieval-app
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the project root and add your API key:
    ```env
    API_KEY=your_secret_api_key
    ```

5. **Run the application**:
    ```sh
    streamlit run app.py
    ```

## Usage

1. **Enter your natural language query** in the input box.
2. **Click the "Submit Query" button** to execute the query.
3. **View the results** displayed on the page.



## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Google Generative AI](https://cloud.google.com/)
- [Python Dotenv](https://pypi.org/project/python-dotenv/)


