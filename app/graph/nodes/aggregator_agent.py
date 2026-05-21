
'''
Author : Junaid Khan 
gets inputsfrom all agents individually and aggregates them into a final review before returning
'''
from app.services.llm_service import generate_review


def aggregator_agent(state):

    final_review = {
        "security": state["security_review"]["findings"],
        "performance": state["performance_review"]["findings"],
        "style": state["style_review"]["findings"],
        "summary": "Multi-agent AI review completed successfully"
    }

    return {
        "final_review": final_review
    }