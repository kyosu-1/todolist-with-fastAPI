from typing import Optional
from app.domains.todo import Todo


class TodoBuilder:

    def __init__(self) -> None:
        self.__todo: Optional[Todo] = None
        self.__session = False
    
    def __call__(self) -> "TodoBuilder":
        assert not self.__session
        self.__session = True
        return self

    def new(
        self,
        title: str,
        description: str,
        deadline,
    ) -> None:
        pass

    def reconstruct_from(self):
        pass

    def build(self):
        pass

