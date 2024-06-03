from core.abstract import Executor


class LinkedInExecutor(Executor):
    def execute(self, *args, **kwargs):
        print('Executing LinkedInExecutor')
        return 'LinkedInExecutor'