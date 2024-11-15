from langchain_community.agent_toolkits.sql.base import create_sql_agent
from langchain_community.agent_toolkits.sql.toolkit import SQLDatabaseToolkit
from langchain_community.utilities import SQLDatabase
from langchain_community.llms.openai import OpenAI
from langchain.chat_models import ChatOpenAI
from langchain.agents import initialize_agent, Tool
from langchain.agents.agent_types import AgentType
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


# Initialize the OpenAI LLM with your API key
llm = OpenAI()

# Initialize the SQL database connection
db = SQLDatabase.from_uri('sqlite:///chinook.db')

# Create the SQL agent toolkit
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Inspect available tools
available_tools = [tool.name for tool in toolkit.get_tools()]
print("Available tools:", available_tools)

# Initialize the ChatOpenAI model
model = ChatOpenAI()

# Define the tools
tools = toolkit.get_tools()

# Initialize the agent
agent = initialize_agent(
    tools, model, agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION, verbose=True
)

# Run the agent to generate a matplotlib bar chart
response = agent.run("generate a matplotlib bar chart of the top 5 countries for sales from the chinook database. Save the output in the current working directory as figure.png")
print(response)
sql_query = """
SELECT BillingCountry AS Country, SUM(Total) AS Sales
FROM invoices
GROUP BY BillingCountry
ORDER BY Sales DESC
LIMIT 5
"""

# Execute the SQL query
conn = sqlite3.connect('chinook.db')
df = pd.read_sql(sql_query, conn)
conn.close()

# Generate the matplotlib bar chart
plt.figure(figsize=(10, 6))
plt.bar(df['Country'], df['Sales'], color='skyblue')
plt.xlabel('Country')
plt.ylabel('Sales')
plt.title('Top 5 Countries for Sales')
plt.savefig('figure.png')
plt.show()