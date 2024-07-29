from core.abstract import Executor


class APIExecutor(Executor):
    def execute(self, *args, **kwargs):
        print('Executing APIExecutor')
        return 'APIExecutor'