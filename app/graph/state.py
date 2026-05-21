from typing import TypedDict, List


class GraphState(TypedDict):

    code: str

    context: str

    security_review: str

    performance_review: str

    style_review: str

    final_review: str