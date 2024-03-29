#! pip install youtube_search

import os

import openai
from langchain.agents import AgentType
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from langchain.tools import YouTubeSearchTool

os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'
openai.api_key = 'YOUR_OPENAI_API_KEY'

tool = YouTubeSearchTool()

tools = [
    Tool(
        name="Search",
        func=tool.run,
        description="useful for when you need to give links to youtube videos. Remember to put https://youtube.com/ "
                    "in front of every link to complete it",
    )
]

agent = initialize_agent(
    tools,
    OpenAI(temperature=0),
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
)

agent.run('Whats a Elon musk video on an interesting topic')
