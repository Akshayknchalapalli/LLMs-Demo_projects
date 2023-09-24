import os

import chainlit as cl
import openai

os.environ['OPENAI_API_KEY'] = 'YOUR_OPENAI_API_KEY'
openai.api_key = 'YOUR_OPENAI_API_KEY'


# return everything that the user inputs.

# pass the message into chatgpt api , .send() the answer.


@cl.on_message
async def main(message: str):
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'assistant', 'content': 'you are a helpful assistant'},
            {'role': 'user', 'content': message}
        ],
        temperature=1,
    )
    await cl.Message(content=f"{response['choices'][0]['message']['content']}", ).send()
