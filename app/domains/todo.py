import datetime
import dataclasses

from app.domains.dateline import Deadline


@dataclasses.dataclass(frozen=False)
class Todo:
    id: int
    title: str
    description: str
    created_at: datetime.datetime
    deadline: Deadline
