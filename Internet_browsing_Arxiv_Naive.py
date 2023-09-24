import os

import openai

# If the parser is erroring out, remember to set temperature to a higher value!!!

# pip install arxiv

os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'
openai.api_key = 'YOUR_OPENAI_API_KEY'

from langchain.chat_models import ChatOpenAI
from langchain.agents import load_tools, initialize_agent, AgentType

llm = ChatOpenAI(temperature=0.0)
tools = load_tools(
    ["arxiv"],
)

agent_chain = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,  ### IMPORTANT
)

agent_chain.run(
    "What is Data Science in software industry",
)
