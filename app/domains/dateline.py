import dataclasses
import datetime


@dataclasses.dataclass(frozen=True)
class Hour:
    value: int

    def __post_init__(self):
        self._validate()

    def _validate(self) -> None:
        if self.value < 0 or self.value > 23:
            raise ValueError("Hour's value must be an integer between 0 and 23")


@dataclasses.dataclass(frozen=True)
class Minute:
    value: int

    def __post_init__(self):
        self._validate()

    def _validate(self) -> None:
        if self.value < 0 or self.value > 60:
            raise ValueError("Minute's value must be an integer between 0 and 60")


@dataclasses.dataclass(frozen=True)
class Deadline:
    date: datetime.date
    hour: Hour
    minute: Minute
