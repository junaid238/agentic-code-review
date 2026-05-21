
'''
Author : Junaid Khan 
gets inputs as state[code] and state[context] from retriever node (inital point in workflow)
genrates a promt using the inputs and sends it to llm_service to generate a reviw(output) using GenAI prompt engineering techniques.
'''
from app.services.llm_service import generate_review
from app.utils.helpers import safe_json_parse

def style_agent(state):

    code = state["code"]
    context = state["context"]

    prompt = f"""
        You are a clean code and Python style expert.

        Use the provided context and coding standards while reviewing the code.

        Context:
        {context}

        Analyze the code for:
        - readability
        - naming conventions
        - maintainability
        - clean code principles
        - dead code
        - formatting issues

        STRICT RULES:
        1. Return ONLY valid JSON
        2. No markdown
        3. No explanations
        4. No intro text
        5. No ```json blocks

        Required JSON format:

        {{
        "findings": [
            {{
            "issue": "example issue",
            "severity": "LOW",
            "recommendation": "example recommendation"
            }}
        ]
        }}

        Code:
        {code}
        """

    review = generate_review(prompt)

    return {
        "style_review": safe_json_parse(review)
    }