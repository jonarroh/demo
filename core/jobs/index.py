from core.abstract import Executor
from core.jobs.impl import Scraper
import pandas as pd
from model.JobListing import JobListing
from storage.mysql.adapter import MySQLAdapter

class JobExecutor(Executor):
    def execute(self, *args, **kwargs):
        result = Scraper.search_jobs(args[0])
        data = pd.DataFrame(result)
        self.save_jobs(data, MySQLAdapter())

        return data.to_dict('records')
    
    def save_jobs(self, jobs: pd.DataFrame, adapter):
        try:
            adapter.connect()
            # Reemplazar valores NaN con None
            jobs = jobs.where(pd.notnull(jobs), None)
            # Convertir el DataFrame en una lista de diccionarios
            jobs_dict = jobs.to_dict(orient='records')
            # Crear instancias de JobListing a partir de los diccionarios
            job_listings = [JobListing(
                company=job.get('company'),
                functions=job.get('criteria', {}).get('Función laboral'),
                sectors=job.get('criteria', {}).get('Sectores'),
                employment_type=job.get('criteria', {}).get('Tipo de empleo'),
                criteria_url=job.get('criteria', {}).get('url'),
                date_posted=job.get('date'),
                location=job.get('location'),
                title=job.get('title'),
                listing_url=job.get('url')
            ) for job in jobs_dict]
            # Guardar instancias en la base de datos
            adapter.saveMany(job_listings)
            adapter.close()
            return True
        except Exception as e:
            print(e)
            return False
