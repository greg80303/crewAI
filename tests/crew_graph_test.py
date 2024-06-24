import pytest

from langgraph.graph import StateGraph

from crewai.crew import Crew
from crewai.graph.state import CrewState
from crewai.graph.taskgraph import TaskGraph
from crewai.process import Process
from crewai.task import Task

from .crew_test import researcher, writer

tasks = [
    Task(
        description="Give me a list of 5 interesting ideas to explore for na article, what makes them unique and interesting.",
        expected_output="Bullet point list of 5 important events.",
        agent=researcher,
    ),
    Task(
        description="Write a 1 amazing paragraph highlight for each idea that showcases how good an article about this topic could be. Return the list of ideas with their paragraph and your notes.",
        expected_output="A 4 paragraph article about AI.",
        agent=writer,
    ),
]


def _create_basic_graph():
    graph = TaskGraph(CrewState)
    graph.add_node("task1", tasks[0])
    graph.add_node("task2", tasks[1])
    graph.add_edge("task1", "task2")
    graph.set_entry_point("task1")
    graph.set_finish_point("task2")
    return graph


def test_crew_wrong_graph_type():
    class GraphState(CrewState):
        my_context: str

    graph = StateGraph(GraphState)

    with pytest.raises(ValueError):
        crew = Crew(
            name="Test Crew",
            process=Process.graph,
            graph=graph,
            tasks=[],
            agents=[],
        )

    return crew


def test_crew_wrong_graph_state_type():
    class GraphState:
        my_context: str

    graph = StateGraph(GraphState)

    with pytest.raises(ValueError):
        crew = Crew(
            name="Test Crew",
            process=Process.graph,
            graph=graph,
            tasks=[],
            agents=[],
        )

    return crew


def test_crew_graph_shouldnt_have_tasks():
    class GraphState(CrewState):
        my_context: str

    graph = TaskGraph(GraphState)

    with pytest.raises(ValueError):
        crew = Crew(
            name="Test Crew",
            process=Process.graph,
            graph=graph,
            tasks=tasks,
            agents=[],
        )

    return crew


def test_crew_graph_dont_set_cgraph():
    class GraphState(CrewState):
        my_context: str

    graph = TaskGraph(GraphState)
    cgraph = graph.compile()

    with pytest.raises(ValueError):
        crew = Crew(
            name="Test Crew",
            process=Process.graph,
            graph=graph,
            cgraph=cgraph,
            tasks=[],
            agents=[],
        )

    return crew
