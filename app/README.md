Agentic Code Review

Agentic Code Review is a project where we use multi-agent systems using LLMs, LangChain, and LangGraph, having built pipelines using RAG architecture, where the system reviews any kind of code and gives suggestions based on code correctness, syntax, and best practices.

Tech Stack
FastAPI
LangChain
LangGraph
OpenAI APIs
RAG (Retrieval-Augmented Generation)
Docker
Python AST (Abstract Syntax Tree)
Project Architecture

For the API layer, we are using FastAPI to manage all the routes.

On the AI layer, we are using LangGraph, LangChain, and OpenAI to write prompts and generate review text.

For correction and reflection on the agent, we are using RAG pipelines to correct the code in real-time without just depending on the context window and the pre-trained model knowledge.

Docker is used for containerization of the entire project as an application.

Folder Structure
agentic-code-review/
│
├── app/
├── api/
├── data/
├── graph/
├── prompts/
├── services/
├── utils/
├── uploads/
├── main.py
└── requirements.txt
Stage 1: File Upload and Processing Pipeline
File Upload

The user uploads the file or code using the upload functionality built with FastAPI.

The uploaded file gets written in bytes format into the uploads/ folder and gets stored there for further processing.

Parser Service (parser.py)

The main purpose of parser.py is to extract the main components of the uploaded code file.

We are utilizing Python's Abstract Syntax Tree (AST), which helps in extracting abstract components from the code such as:

Classes
Imports
Alias Imports
Functions

The parser.py file returns a list of:

Functions
Classes
Imports
Aliases

from the uploaded code file.

Chunking Service (chunker.py)

Since the code files can be massive and extensive, we are chunking the files into smaller chunks of code.

chunk_size is passed as a parameter to the chunker so that it splits the entire code into different chunks and returns snippets of code as chunks.

These chunks are utilized by parser.py to parse the data efficiently.

chunker.py is called inside parser.py and returns the chunks for further processing.

API Routes (routes.py)

We are making a dedicated file to define all the API routes used as part of FastAPI.

The upload functionality is written as a coroutine using asynchronous programming because it involves I/O operations.

By using async, the wait time of the program is reduced, and the server can simultaneously accept uploads from other users without waiting for the first request to complete.

Hence, the upload functionality is implemented asynchronously for better performance and scalability.

All the API routes are defined in routes.py and are called in main.py, where the FastAPI application is initialized.


Stage 2: Integration of AI Layer with Backend
AI Layer Integration using FastAPI

Step 2: Integration of the AI layer with the backend layer we built using API and FastAPI.

We'll create a .env file and store our OpenAI key or Gemini key or Groq key. We use .env and declare it in the .gitignore file so that the key is not hardcoded anywhere in the code. This provides secrecy, encapsulates the key, and keeps it private.

LLM Service Creation

Now we'll create an LLM service where we initialize the model using:

API key
Model name
Temperature

We set the temperature as 0.

In this case, we use temperature as 0 to avoid randomness and improve consistency.

We initialize the LLM model using the model name and temperature. Then we invoke the model by passing in the prompt.

We use the prompt defined in prompts.txt and pass it as a parameter to invoke the LLM model and return the response.

Prompt Engineering

We create a prompt.txt file under:

app/prompts/prompt.txt

A machine prompt is written to instruct the LLM to perform its activities and define its responsibilities.

Here, we are creating a security-specific prompt to check:

Security vulnerabilities
Database injections
Authentication issues

The model will provide:

Issue
Recommendation
Severity of the issue

We also have a formatted section at the bottom of the prompt to pass the code as a parameter.

Building reviewer.py

Now we start building reviewer.py.

reviewer.py has two components:

1. Loading the Prompt

For loading the prompt, we use the prompt.txt file which we just built.

2. Review Code

Here we:

Take the prompt template
Take the code chunk
Pass it into the prompt
Generate a review using the final prompt
Return the review

generate_review() is used from the LLM service, which invokes the LLM model and returns the response.

FastAPI Route Integration

We use this review_code method and import it into routes.py.

We create a response object for this, and return the AI review by calling the review_code method from the LLM service.

At this point, our app acts as an agent which:

Takes code as input
Uses machine prompts from prompt.txt
Generates a review using the LLM service
Routes it back as a response using FastAPI
Response Schemas

To make the response more specific, we define schemas under:

app/schemas.py

We define a schema which has three components:

Issues
Severity
Recommendation