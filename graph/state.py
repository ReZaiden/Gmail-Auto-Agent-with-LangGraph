from pydantic import BaseModel
from typing import Annotated, Any
from langgraph.graph.message import add_messages

# Simple State Schema
class State(BaseModel):
    messages: Annotated[list[Any], add_messages]
