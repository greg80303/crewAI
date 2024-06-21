from typing import Type

from langgraph.graph import StateGraph
from pydantic import validate_arguments

from crewai.graph.state import CrewStateType


class TaskGraph(StateGraph):
    """A Crew process graph that has Tasks as nodes and CrewState (or a class derviced from it) as the state

    When instantiating your Crew with ProcessType `graph`, you must also provide an instance of this class
    """

    @validate_arguments
    def __init__(self, state_schema: Type[CrewStateType], **kwargs):
        super().__init__(state_schema=state_schema, **kwargs)
