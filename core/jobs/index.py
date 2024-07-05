from core.abstract import Executor
from core.jobs.impl import Scraper


class JobExecutor(Executor):
    def execute(self, *args, **kwargs):
        result = Scraper.search_jobs(args[0])
        return result.to_dict('records')