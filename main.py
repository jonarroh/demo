from core.scraper import scrappProfiles,scrapp_jobs,search_people
from model.config import Config

dict = {
  "keywords": "vue",
  "location": "León,Gto",
}



if __name__ == "__main__": 
  search_people(dict)           
  #config = Config(**dict)
  # scrappProfiles(config.__dict__)
  #scrapp_jobs(config.__dict__)
