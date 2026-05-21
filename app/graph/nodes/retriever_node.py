
'''
Author : Junaid Khan 
takes in state[code] as input generates context by passing code as query to retriever.py and returns the state[context]

'''
from app.services.retriever import retrieve_context


def retriever_node(state):

    code = state["code"]

    context = retrieve_context(code)

    state["context"] = context

    return {
        "context": context
    }