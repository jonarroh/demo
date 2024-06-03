from typing import TypeVar, Optional
from dataclasses import dataclass

T = TypeVar('T')

@dataclass
class Result:
    value: Optional[T] = None
    error_message: Optional[str] = None
    is_ok: bool = False

    def ok(self, value: T) -> 'Result':
        self.value = value
        self.is_ok = True
        return self
    
    def err(self, error: str) -> 'Result':
        self.error_message = error
        return self
    
    def is_error(self) -> bool:
        return not self.is_ok

    def __str__(self):
        if self.is_ok:
            return f"Ok({self.value})"
        return f"Error({self.error_message})"