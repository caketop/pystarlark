from typing import Optional

class StarlarkGo:
    def __init__(self) -> None: ...
    def eval(
        self, expr: str, filename: Optional[str] = ..., parse: Optional[bool] = ...
    ) -> str: ...
    def exec(self, defs: str, filename: Optional[str] = ...) -> None: ...
