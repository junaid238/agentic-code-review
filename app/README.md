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