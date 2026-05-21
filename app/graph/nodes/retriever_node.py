from app.services.retriever import retrieve_context


def retriever_node(state):

    code = state["code"]

    context = retrieve_context(code)

    state["context"] = context

    return {
        "context": context
    }