# LLM Demo Projects
## What are LLM Models?
LLM stands for Large Language Model. LLM models are AI systems trained on vast amounts of text data using a technique called transformer architecture. Some examples of popular LLM models are:
- GPT-3 by OpenAI
- BERT by Google
- Megatron by NVIDIA

#### The key characteristics of LLMs are:

1. They are trained on massive amounts of text data - up to hundreds of billions of words
2. They learn the statistical relationships between words and concepts from the training data
3. They can generate text that resembles the text they were trained on

#### This text generation ability enables LLMs to be used for tasks like:
- Autocompletion
- Text summarization
- Question answering
- Chatbots
## What is Langchain?
Langchain is an open-source library that makes it easy to build tools and agents using LLM models. Some key features of Langchain are:
- Toolkits to integrate with popular LLM models like GPT-3, BERT, etc.
- APIs to build tools, agents and chatbots using LLMs
- Capabilities like text generation, classification, summarization, etc.
- Built-in support for agent types like zero-shot, few-shot and dual-encoder agents
#### With Langchain, you can:
- Prompt LLM models from your Python code
- Add custom tools to your agents
- Build workflows by chaining multiple tools and LLMs
- Deploy your agents as APIs, CLI tools, web apps, etc.

Langchain provides an abstraction layer on top of LLM models that makes them easy to integrate and use for building applications.

LLMs provide the core text generation and understanding capabilities, while Langchain makes it simple to build tools and agents that utilize those LLM capabilities.

# Table of Contents

1. [Project 1: Building a Chatbot with Chainlit(#v1.0)🚀🤖](#project-1-building-a-chatbot-with-chainlitv10)
2. [Project 2: Integrating Chatbot with Langchain via Chainlit (#v1.1)🚀🤖](#project-2-integrating-chatbot-with-langchain-via-chainlit-v11)
3. [Hands-on with Chroma-DB](#hands-on-with-chroma-db)
4. [Project 3: Efficient Document Question Answering System](#project-3-efficient-document-question-answering-system)
5. [Project 4: Efficient Research Paper Parsing using Agent](#project-4-efficient-research-paper-parsing-using-agent)
6. [Project 5: Seamless Internet Browsing with Chainlit](#project-5-seamless-internet-browsing-with-chainlit)
7. [Project 6: Human-Aided AI Enhancement Project](#project-6-human-aided-ai-enhancement-project)
8. [Project 7: Python Replit Agent](#project-7-python-replit-agent)
9. [Project 8: Youtube Search Agent](#project-8-youtube-search-agent)
10. [Project 9: Enhanced Text Generation with AI](#project-9-enhanced-text-generation-with-ai)
11. [Project 10: A Python REPL Tool with Integrated YouTube Video](#project-10-a-python-repl-tool-with-integrated-youtube-video)
12. [Project 11: Equipping LLMs Custom Tool Creation in Langchain](#project-11-equipping-llms-custom-tool-creation-in-langchain)


# Project 1:  Building a Chatbot with Chainlit(#v1.0)🚀🤖
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
5. It automatically creates a `chainlit.md` file which displays content when we run the code. You can edit as you like if you wish.

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

# Project 2: Integrating chatbot with Langchain via Chainlit (#v1.1)🚀🤖"
This project contains code that generates automated responses using OpenAI's GPT-3 API built with chailit using Langchain Integration

## Technologies
- `lanchain` - An open source framework for building custom knowledge chatbots. We will use LangChain to integrate GPT-3 with external data.
- `Chainlit` - A Python framework for building UI on top of any Python code. We will use Chainlit to provide a conversational interface for our chatbot.


## Setup
1. Install the required libraries - chainlit and openai and langchain

        pip install chainlit openai
        pip install langchain
2. Create an OpenAI API key and add it as an environment variable
3. Define your prompt template and create your LangChain:
4. Call your LangChain from Chainlit:
5. Run your chatbot:

        chainlit run langchain_integration.py
    **Note:** run the python file in command prompt or terminal but not on any python IDEs.
6. Interact with your chatbot! It will provide GPT-3 responses to your questions.

## Usage
To use the code:
1. Sets the **OPENAI_API_KEY** environment variable with your `openAI API key`. (If not already exists create one from openai.com)
2. Import the required Libraries
3. LLMChain is most basic building block chain. It takes in a prompt template, formats it with the user input and returns the response from an LLM.
4. now create a very simple chain that will take user input, format the prompt with it, and then send it to the LLM.

## Future Improvements
- Using VectorDB and embeddings in LangChain
- Chaining multiple LLMs together

# Hands on with Chroma-DB
Chroma DB is an open source embedding database that can be used to store and retrieve vector embeddings efficiently. This README will cover how to integrate Chroma DB into your application.

## Setup
You can install Chroma DB using pip:

    pip install chromadb
Chroma DB also has a standalone server that you can run.

## How it works
### Creating a Client
- To connect to a Chroma DB database, you first create a client:
### Creating a Collection
- Next, you create a collection which is similar to a table:
- You can then add text documents to this collection along with metadata and IDs:
- Chroma DB will automatically embed the text into vectors using a default model.
### Querying the Collection
- You can query the collection using natural language:
- Chroma DB will embed the query and return the most similar documents based on vector similarity.

# Project 3: Efficient Document Question Answering System

This project implements a document question answering system that can answer questions about PDF and text files.

## How to use
To use the chatbot:
1. Install the module pypdf

        pip install pypdf
2. Run the following command to start the chatbot:
        
        chatlit run document_qa.py

3. Upload a PDF or text file using the chatbot interface
4. The file will be split into chunks to allow for better question answering
5. Ask questions about the content of the uploaded file
6. The chatbot will try to find relevant text passages from the file as sources for the answer

# Improvements
Some ways to improve the project further:

- Support more document formats (DOCX, TXT, HTML)
- Add co-reference resolution
- Handle complex questions using syntactic parsing
- Provide context-aware responses
- Train a custom QA model for domain-specific documents

# Project 4: Efficient Research Paper Parsing using agent
This project parses research papers from arXiv and extracts useful information.

## Features
- Parses PDF research papers downloaded from arXiv using `ZERO_SHOT_REACT_DESCRIPTION` algo
- Extracts metadata like title, authors, abstract, sections, references etc.
- Outputs data in JSON format for easy parsing
- Command line interface for batch processing of papers
- Can be integrated as a library in your own projects

## How it Works
this file **Intenet_browsing_Arvix_Naive.py** uses machine learning models trained on labeled data to identify the different sections and elements in a research paper. It handles PDFs as input and outputs a structured JSON containing:

- Paper title
- Author list
- Abstract text
- Section headings and body text
- References with:
    - Title
    - Authors
    - Venue
    - Year
- Mentions of references within the paper text

This structured format makes it easy to process the information from the paper programmatically.

## Usage
You can either:
1. Use the CLI to parse papers from the command line
2. Integrate the library into your own Project by installing **arvix**

         pip install arxiv
    
3. Access the parser using a open_api_key
4. run the project file:


# Project 5: Seamless Internet Browsing with Chainlit
This project uses Chainlit to build an application that allows users to browse the internet from a Unified chainlit UI Experience.

## How it works
The **internet_browsing_chainlit.py**  file contains a Chainlit app with the following functionality:
- When a user inputs a URL, the app passes it to a headless browser tool that loads the webpage
- The tool extracts relevant information from the webpage like:

    - Title
    - Headers
    - Paragraphs
    - Images
- This information is passed back to the Chainlit app and displayed to the user in an organized manner
- The user can then:
    - Click on images to view them in full screen
    - Click on links to load that URL in the headless browser
- The app utilizes a headless browser tool like Playwright to load webpages and extract information.
- The app then displays the extracted information to the user in an organized manner within the Chainlit UI. Users can interactively load new URLs, view images and click on links.
- This allows for a conversational interface for browsing the internet without leaving the Chainlit UI.

## Future Improvements
Some ways to improve this project further:

- Add more search engines (Bing, DuckDuckGo)
- Support image/news search
- Allow opening multiple URLs
- Handle more complex questions using NLP models
- Provide relevant contextual responses

# Project 6: Human-Aided AI Enhancement Project
This project aims to augment AI systems with human intelligence in a scalable way. It does this by:

## What does this project do?
This project `Human_as_a_tool.py` uses a human assistant to provide information and perform tasks. It does this by:

- Reading a web search result provided by the human 
- Answering questions based on the content
Providing code examples to illustrate concepts
- The goal is to utilize the human's intelligence and knowledge to augment the capabilities of the Python script.

The end goal is to provide AI systems with a scalable source of high-quality human input to improve their performance.

Some example tasks include:

- Labeling data for machine learning models
- Correcting AI generated text
- Answering factual questions
- Providing commonsense knowledge

## How to use it
To use thi chatbot:

1. Run the Python file:

2. The script will ask you to provide a web search result

3. Copy/paste the result into the provided format
4. The script will then ask a question related to the content
5. It will format your answer into markdown, providing code examples where relevant

The script relies on you, the human, to provide the relevant information and knowledge. It simply structures that information in a useful way.

## Limitations
- The script cannot evaluate the accuracy or quality of the information you provide
- It is unable to perform the tasks itself, only format your responses
- The questions it can answer are limited to the web search result you supply

With more advanced NLP and knowledge models, the limitations could be reduced over time. But for now, it heavily depends on a human assistant.

# Project 7: Python Replit Agent
This Python script creates an agent that can interact and execute code in a Python REPL environment.

This project contains Python code run on Repl.it.

### What is Repl.it?
Repl.it is an online code editor that allows you to write and run code, as well as collaborate with others in real time. Some key features:

- Run code in over 45 languages directly in the browser
- Host web apps and access them from a custom URL
- Collaborate with teams in real time
- Integrate with GitHub, GitLab and Bitbucket
### Repl.it is perfect for:

- Learning to code
- Web development projects
- Open source contributions
- Hosting small web apps

## How to use
- Install the dependencies
- To run the script:
- Set your OpenAI API key as an environment variable:
- Run the script:

The agent will ask "What is the 10th fibonacci number?". It uses OpenAI's GPT-3 model for natural language understanding and the PythonREPLTool to execute code in a REPL.

## Limitations
- The agent can currently only answer one question
- It uses a generalist model so performance may vary
- The REPL environment is simple

Improvements could include:

- Training a task-specific model
- Using multiple tools to answer questions
- Improving the REPL environment

# Project 8: Youtube Search Agent
This Python script utilizes an OpenAI model and a YouTube search library to create a simple search engine for YouTube videos.

## How it works
- The script initializes an OpenAI language model and imports the **youtubesearchTool** library. It then creates an agent that can react to user input and search YouTube.

- When the user provides a search query, the agent passes the query to youtubesearchpython which finds relevant YouTube videos and returns their URLs. The agent then responds to the user with the YouTube video URLs.

## Setup
- Install requirements:

        pip install youtube_search


## Usage
- Run the script:
    
        chainlit run Youtube_searchpy

- Provide a YouTube search query:
- The agent will respond with relevant YouTube video URLs
- Click the links to watch the videos!
- You can also limit the number of results
- And filter by date, relevance, viewCount etc. See youtubesearchpython docs for options.

## Limitations
- The OpenAI model provides general purpose search, so performance depends on its capabilities.
- The search results depend on how **youtubesearchTool** queries YouTube.
The agent cannot currently answer follow up questions.

# Project 9: Enhanced Text Generation with AI

This project contains a command-line tool for generating text using an AI agent powered by GPT.

## Some key features:

- Prompt the AI agent with any text query using `CHAT_ZERO_SHOT_REACT_DESCRIPTION` algorithm.
- Generate creative and accurate text responses in an AI-assisted writing manner using `shellTool` method
- It automatically creates a **.txt** with the solution for the given question input(e.g empty.txt)
- Ability to use different GPT models (e.g GPT-3, GPT-4)
- Command-line interface for easy integration into scripts and workflows
- run the script:

# Project 10:  A Python REPL Tool with Integrated YouTube Video
This tool combines a Python REPL environment with the ability to search YouTube for relevant video demonstrations.

## How it works
The tool consists of two parts:

1. A Python REPL agent built using the langchain library. This allows the user to interactively execute Python code **Combination_of_both.py**.

2. A YouTube search agent that can search YouTube for relevant video tutorials.

When the user provides Python code, the REPL agent executes it and provides output. If the user requests a video explanation, the YouTube search agent searches for relevant videos and returns their URLs.

## Usage
To use the tool:
- Run the script:
- Provide Python code to the REPL agent
- Request a video explanation
- The agent will respond with relevant YouTube video URLs
- Click the links to watch the video tutorials!

# Project 11: Equipping LLMs Custom Tool Creation in Langchain

This project **custom_tools.py** demonstrates how to define and use custom tools with Langchain.

## Multiplier Tool
**Multiplier** - A tool that takes two numbers as input, separated by a comma, and returns their product. For example, an input of "3,4" would return 12.

## Summary
- Define the actual logic in a function
- Define a parsing function to convert user input into arguments for the logic function
- Define the tool with a name, functions, and description
- Initialize an agent with the tool
- Run the agent to use the tool

define the tool's logic, parsing, and details, then initialize the agent with that tool. When the agent runs, it executes the tool's function based on the user input.

