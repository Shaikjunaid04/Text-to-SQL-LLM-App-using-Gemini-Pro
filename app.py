from dotenv import load_dotenv
load_dotenv() #load all the enviroment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

#configure our API KEY
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


#Function to Load Google Gemini MOdel and provide Sql query as response : 

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text


#function to retrieve query from the SQL Database

def read_sql_query(sql, db):
    try:
        conn = sqlite3.connect(db)
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        conn.commit()
        return rows
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        return None
    finally:
        conn.close()



#Define Prompt 

prompt=[
    
    """
    You are an expert in converting English Questions to SQL Query!
    The SQL Database has the name STUDENT and has the following columns - NAME, CLASS,
    SECTION and MARKS \n\nFor example,\nExample 1- How many entries of records are present?,
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data science class ? , 
    the SQL command will be something like tis SELECT * FROM STUDENT
    where CLASS ='Data Science";
    also the sql code should not have ``` in beginning or end and sql word in output
    """
]

### streamlit app 
# Set the page configuration (must be the first Streamlit command)
st.set_page_config(page_title="SQL Query Retriever", page_icon="📊")

# Add a title and description
st.markdown("<h1 style='color: black;'>Gemini SQL Data Retrieval App</h1>", unsafe_allow_html=True)
st.markdown("""
    <div style='color:black;'>
        Welcome to the Gemini App! This application allows you to retrieve data from a SQL database using natural language queries.
        Simply enter your query below, and click 'Submit Query' to see the results.
    </div>
""", unsafe_allow_html=True)

# Add a text input field for the query
question = st.text_input("Enter your SQL query:", key="input")

# Add a submit button
if st.button("Submit Query"):
    response = get_gemini_response(question, prompt)  # Assuming get_gemini_response is defined
    st.markdown(f"<div style='color: white;'>Executing SQL query:</div>", unsafe_allow_html=True)
    st.code(response, language='sql')
    
    data = read_sql_query(response, "student.db")
    
    if data:
        st.success("Query executed successfully! Here are the results:")
        for row in data:
            st.write(row)
    else:
        st.error("No data retrieved or an error occurred.")

# Footer
st.markdown("---")

# Optional: Add some CSS for better styling and background color
# Optional: Add some CSS for better styling and background color
st.markdown("""
    <style>
    .main {
        background-color: #f0f0f0;  /* Light background color */
        padding: 20px;
    }
    .stTextInput > div > input {
        font-size: 16px;
        padding: 10px;
        color: #000000;  /* Black text color */
        background-color: #ffffff;  /* White background color for input */
    }
    .stButton > button {
        background-color: #4CAF50;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
    }
    .stMarkdown div {
        color: #000000;  /* Black text color for markdown */
    }
    .stAlert > div {
        color: #000000;  /* Black text color for alerts */
    }
    </style>
""", unsafe_allow_html=True)