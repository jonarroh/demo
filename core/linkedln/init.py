from core.abstract import Executor
from core.linkedln.impl import Scraper
from storage.mysql.adapter import MySQLAdapter
from model.LinkedinProfile import LinkedInProfile
from pandas import DataFrame
import pandas as pd

class LinkedInExecutor(Executor):
    def execute(self, *args, **kwargs):
        return 'this is currently not implemented'
        result = Scraper.search_people(args[0])
        itWork = self.save_profiles(result, MySQLAdapter())
        print("se guardo el perfil")
        if itWork:
            return result.to_dict('records')
        else:
            return None
    
    def save_profiles(self, profiles: DataFrame, adapter):
        try:
            adapter.connect()
            profiles = profiles.where(pd.notnull(profiles), None)
            profiles = profiles.to_dict(orient='records')
            profiles = [LinkedInProfile(**profile) for profile in profiles]
            adapter.saveMany(profiles)
            adapter.close()
            return True
        except Exception as e:
            print(e)
            return False