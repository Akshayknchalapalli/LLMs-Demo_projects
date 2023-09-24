# https://python.langchain.com/docs/modules/agents/tools/multi_input_tool

import os

import chainlit as cl
import openai
from langchain.agents import AgentExecutor
from langchain.agents import AgentType
from langchain.agents import initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import ShellTool

shell_tool = ShellTool()

os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'
openai.api_key = 'YOUR_OPENAI_API_KEY'


@cl.on_chat_start
def start():
    llm = ChatOpenAI(temperature=0)

    shell_tool.description = shell_tool.description + f"args {shell_tool.args}".replace(
        "{", "{{"
    ).replace("}", "}}")

    agent = initialize_agent(
        [shell_tool],
        llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
        handle_parsing_errors=True
    )
    cl.user_session.set("agent", agent)


@cl.on_message
async def main(message):
    agent = cl.user_session.get("agent")  # type: AgentExecutor
    cb = cl.LangchainCallbackHandler(stream_final_answer=True)

    await cl.make_async(agent.run)(message, callbacks=[cb])
