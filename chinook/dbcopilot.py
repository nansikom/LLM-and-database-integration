import streamlit as st
from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase


#from langchain_community.llms import OpenAI
from langchain_community.llms.openai import OpenAI
from langchain_openai import OpenAI
from langchain_community.chat_models import ChatOpenAI



#from langchain.sql_database import SQLDatabase
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType

from langchain.agents import initialize_agent, Tool
from langchain.agents import AgentType
#from streamlit_chat import message as st_chat_message
import streamlit as st
from langchain_community.callbacks.streamlit import StreamlitCallbackHandler
import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
st.set_page_config(page_title="DBCopilot", page_icon=" ")
st.header(' Welcome to DBCopilot, your copilot for structured databases.')
load_dotenv()
#openai_api_key = os.environ['OPENAI_API_KEY']
db = SQLDatabase.from_uri('sqlite:///chinook.db')
llm = OpenAI()
db = SQLDatabase.from_uri('sqlite:///chinook.db')

toolkit = SQLDatabaseToolkit(db=db, llm=llm)
tool_names = [tool.name for tool in toolkit.get_tools()] 
prompt_prefix = f"You are an agent designed to interact with a SQL database. Available tools: {', '.join(tool_names)}"

prompt_format_instructions = "Question: the input question you must answer"


agent_executor = create_sql_agent(
 prefix=prompt_prefix,
 format_instructions = prompt_format_instructions,
 llm=llm,
 toolkit=toolkit,
 verbose=True,
 top_k=10
)
if "messages" not in st.session_state or st.sidebar.button("Clear message history"):
 st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])
if user_query:
    st.session_state.messages.append({"role": "user", "content": user_query})
    st.chat_message("user").write(user_query)

with st.chat_message("assistant"):
    st_cb = StreamlitCallbackHandler(st.container())
    response = agent_executor.run(user_query, callbacks = [st_cb], handle_parsing_errors=True)
st.session_state.messages.append({"role": "assistant", "content": response})
st.write(response)