# Lang chain is using this to interact with the SQL database class allowing u to interact with the database using the OpenAI model
# create an agent that can interact with the DB
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

llm = OpenAI()
db = SQLDatabase.from_uri('sqlite:///chinook.db')
toolkit = SQLDatabaseToolkit(db=db, llm=llm)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)
print([tool.name for tool in toolkit.get_tools()])
#results=agent_executor.run("Describe the playlisttrack table")
#print(results)
agent_executor.run("DEscribe the playlisttrack table ")

result = agent_executor.run("What are the top 5 best-selling albums and their artists?")
print(result)

 
#from langchain.chat_models import ChatOpenAI

