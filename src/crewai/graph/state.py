from typing import Any, Optional
from pydantic import Field


class CrewState:
    """
    Tracks the state of crew execution when using the 'graph' process type. Custom
    crew state objects must derive from this class
    """

    context: Optional[Any] = Field(
        description="Simple context passed between Tasks during crew execution. By default all Tasks will read their input context from this field before execution and write their output to this field after execution.",
        default="",
    )
