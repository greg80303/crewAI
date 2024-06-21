from typing import Any, Optional, TypeVar
from pydantic import BaseModel, Field


class CrewState(BaseModel):
    """
    Tracks the state of crew execution when using the 'graph' process type. Custom
    crew state objects must derive from this class
    """

    context: Optional[Any] = Field(
        description="Simple context passed between Tasks during crew execution.",
        default="",
    )


CrewStateType = TypeVar("CrewStateType", bound=CrewState)
