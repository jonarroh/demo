from core.abstract import Executor
from core.linkedln.impl import Scraper

class LinkedInExecutor(Executor):
    def execute(self, *args, **kwargs):
        scrapper = Scraper.search_people(args[0])
        return "LinkedInExecutor"