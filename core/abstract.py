from abc import ABC, abstractmethod
"""
An abstract class that represents an executor.

The execution method must be implemented by the subclasses that want to be executors by the rpa system.

THIS CLASS SHOULD NOT BE MODIFIED.

"""
class Executor(ABC):
    @abstractmethod
    def execute(self, *args, **kwargs):
        pass