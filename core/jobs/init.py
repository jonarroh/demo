from core.abstract import Executor
from core.jobs.core import Scraper
import pandas as pd
from model.JobListing import JobListing
from storage.mysql.adapter import MySQLAdapter
import datetime
class JobExecutor(Executor):
    def execute(self, *args, **kwargs):
        result = Scraper.search_jobs(args[0])
        data = pd.DataFrame(result)
        self.save_jobs(data, MySQLAdapter())
        print("JobExecutor executed")
        return data.to_dict('records')
    
    def save_jobs(self, jobs: pd.DataFrame, adapter):
        try:
            adapter.connect()
            # Reemplazar valores NaN con None
            jobs = jobs.where(pd.notnull(jobs), None)
            # Convertir el DataFrame en una lista de diccionarios
            jobs_dict = jobs.to_dict(orient='records')
            # Crear instancias de JobListing a partir de los diccionarios
            created_at =  datetime.datetime.now()
            job_listings = [JobListing(
                company=job.get('company'),
                functions=job.get('criteria', {}).get('Función laboral') if job.get('criteria') else 'n/a',
                sectors=job.get('criteria', {}).get('Sectores') if job.get('criteria') else 'n/a',
                employment_type=job.get('criteria', {}).get('Tipo de empleo') if job.get('criteria') else 'n/a',
                criteria_url=job.get('criteria', {}).get('url') if job.get('criteria') else 'n/a',
                date_posted=job.get('date'),
                location=job.get('location'),
                title=job.get('title'),
                listing_url=job.get('url'),
                created_at=created_at
            ) for job in jobs_dict]
            # Guardar instancias en la base de datos
            adapter.saveMany(job_listings)
            adapter.close()
            return True
        except Exception as e:
            print(e)
            return False
