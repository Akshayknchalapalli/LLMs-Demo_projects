# chatbot with Chainlit🚀🤖
This project contains a simple GPT-3 based chatbot built using the Chainlit framework and OpenAI Chat Completion API.

## Technologies Used
- `Chainlit` - A Python framework for building Discord bots. We use Chainlit to receive user messages and send responses.

- `OpenAI Chat Completion API` - We use OpenAI's GPT-3 model to generate responses to user messages.

## Files
- `main.py` - Contains the code for the chatbot that receives a user message and sends the GPT-3 generated response.

## Setup
1. Install the required libraries - **chainlit** and **openai**

         pip install chainlit openai
2. Create an OpenAI API key and add it as an environment variable
3. Run the **main.py** file
            
        chainlit run main.py
- **Note:** run the python file in command prompt or terminal but not on any python IDEs.
4. Interact with the bot!

## How it works
The script does the following:
1. Sets the **OPENAI_API_KEY** environment variable with your `OpenAI API key`.(If not already exists create one from openai.com)
2. Imports the **chainlit** and **openai** libraries
3. Defines a function that is triggered whenever a new message is received
4. The function takes the user's message and sends it to the OpenAI Chat Completion API
5. It retrieves the response from OpenAI and sends it back to the user using Chainlit
6. The bot introduces itself as a `helpful assistant` and then responds to the user's message.

## Future Improvements
- Add more GPT-3 models for varied responses
- Fine tune a GPT-3 model specifically for the chatbot's use case
- Add features like sentiment analysis, entity extraction, and fact checking.