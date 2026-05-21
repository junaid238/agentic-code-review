from langgraph.graph import StateGraph, END

from app.graph.state import GraphState

from app.graph.nodes.retriever_node import retriever_node
from app.graph.nodes.security_agent import security_agent
from app.graph.nodes.performance_agent import performance_agent
from app.graph.nodes.style_agent import style_agent
from app.graph.nodes.aggregator_agent import aggregator_agent


workflow = StateGraph(GraphState)

# Nodes
workflow.add_node("retriever", retriever_node)

workflow.add_node("security", security_agent)

workflow.add_node("performance", performance_agent)

workflow.add_node("style", style_agent)

workflow.add_node("aggregator", aggregator_agent)

# Entry Point
workflow.set_entry_point("retriever")

# Edges
workflow.add_edge("retriever", "security")
workflow.add_edge("retriever", "performance")
workflow.add_edge("retriever", "style")

workflow.add_edge("security", "aggregator")
workflow.add_edge("performance", "aggregator")
workflow.add_edge("style", "aggregator")

workflow.add_edge("aggregator", END)

graph = workflow.compile()