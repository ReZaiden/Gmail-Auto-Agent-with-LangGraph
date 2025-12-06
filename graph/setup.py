from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode

import uuid
from typing import Dict, Any, List, Optional

from tools.gmail_tools import get_gmail_tools
from utils.config import Config
from graph.state import State

# Graph -> A graph for assist user to manage gmail account
class Graph:
    def __init__(self):
        self.gmail_agent = None
        self.gmail_instructions = None
        self.gmail_tools = None
        self.graph = None
        self.db = MemorySaver()
        self.thread_id = str(uuid.uuid4())

    # setup -> setup the graph and create gmail_agent with tools
    async def setup(self):
        self.gmail_tools = await get_gmail_tools()
        self.gmail_instructions = Config.agents_config()['gmail_agent']['instructions']
        gmail_agent = ChatOpenAI(model=Config.agents_config()['gmail_agent']['model'])
        self.gmail_agent = gmail_agent.bind_tools(self.gmail_tools)
        await self.build_graph()

    # gmail_agent_node -> process the gmail agent
    def gmail_agent_node(self, state: State) -> Dict[str, Any]:
        responses = self.gmail_agent.invoke(state.messages)
        return {
            'messages': [responses],
        }

    def gmail_tools_condition(self, state: State) -> str:
        last_message = state.messages[-1]
        if hasattr(last_message, "tool_calls") and last_message.tool_calls:
            return "gmail_tools"
        else:
            return "__end__"

    # build_graph -> build the graph with nodes and edges
    async def build_graph(self):
        graph_builder = StateGraph(State)

        graph_builder.add_node('gmail_agent', self.gmail_agent_node)
        graph_builder.add_node('gmail_tools', ToolNode(self.gmail_tools))

        graph_builder.add_edge(START, 'gmail_agent')
        graph_builder.add_conditional_edges('gmail_agent', self.gmail_tools_condition, {'gmail_tools': 'gmail_tools', '__end__': END})
        graph_builder.add_edge('gmail_tools', 'gmail_agent')

        self.graph = graph_builder.compile(checkpointer=self.db)

    # run -> run the super step of the graph
    async def run(self, message: Any, history: Optional[List[Any]]=None):
        state = {
            'messages': message,
        }
        response = await self.graph.ainvoke(state, config={"configurable": {"thread_id": self.thread_id}})
        return response
