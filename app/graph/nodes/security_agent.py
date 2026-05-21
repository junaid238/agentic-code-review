from app.graph import state
from app.services.llm_service import generate_review
from app.utils.helpers import safe_json_parse


def security_agent(state):

    code = state["code"]

    context = state["context"]

    prompt = f"""
        You are a security expert.

    Analyze the code for:
    - SQL injection
    - hardcoded secrets
    - unsafe code practices
     using the  {context} as reference for best practices.

    STRICT RULES:
    1. Return ONLY valid JSON
    2. No markdown
    3. No explanation
    4. No intro text
    5. No ```json blocks

    Required format:

    {{
    "findings": [
        {{
        "issue": "SQL Injection",
        "severity": "HIGH",
        "recommendation": "Use parameterized queries"
        }}
    ]
    }}

    Code:
    {code}
    """

    review = generate_review(prompt)

    return {
        "security_review": safe_json_parse(review)
    }