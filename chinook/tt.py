from dotenv import load_dotenv
import os
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_community.llms.openai import OpenAI
from langchain_openai import OpenAI

from langchain_community.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from streamlit_chat import message as st_chat_message
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler






# Load environment variables from a .env file
load_dotenv()

# Initialize the OpenAI LLM with your API key from the environment variable
llm = OpenAI()

# Initialize the SQL database connection
db = SQLDatabase.from_uri('sqlite:///chinook.db')

# Create the SQL agent toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Inspect available tools
available_tools = [tool.name for tool in toolkit.get_tools()]
print("Available tools:", available_tools)

# Define prompt prefix and format instructions
prompt_prefix = f"You are an agent designed to interact with a SQL database. Available tools: {', '.join(available_tools)}"
prompt_format_instructions = "Question: the input question you must answer"

# Create the SQL agent
agent_executor = create_sql_agent(
    prefix=prompt_prefix,
    format_instructions=prompt_format_instructions,
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    top_k=10,
   
)



# Streamlit chat interface
st.set_page_config(page_title="DBCopilot", page_icon=" ")
st.header('Welcome to DBCopilot, your copilot for structured databases.')

if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
for msg in st.session_state.messages:
    st_chat_message(msg["role"]).write(msg["content"])

user_query = st.text_input("Enter your query here:")
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st_chat_message("user").write(user_query)

    with st.chat_message("assistant"):
        st_cb = StreamlitCallbackHandler(st.container())
        response = agent_executor.run(user_query, callbacks=[st_cb], handle_parsing_errors=True)
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.write(response)  







