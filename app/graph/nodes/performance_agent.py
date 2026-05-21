from app.services.llm_service import generate_review
from app.utils.helpers import safe_json_parse

def performance_agent(state):

    code = state["code"]

    context = state["context"]

    prompt = f"""
    You are a performance optimization expert.

    Use the following coding standards and best practices context
    while reviewing the code.

    Context:
    {context}

    Analyze the code for:
    - inefficient loops
    - memory issues
    - blocking operations
    - scalability problems

    STRICT RULES:
    1. Return ONLY valid JSON
    2. No markdown
    3. No explanations
    4. No intro text

    Required format:

    {{
      "findings": [
        {{
          "issue": "",
          "severity": "",
          "recommendation": ""
        }}
      ]
    }}

    Code:
    {code}
    """

    review = generate_review(prompt)

    return {
        "performance_review": safe_json_parse(review)
    }