from sqlalchemy import Column, String, Text, DateTime,Integer
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class JobListing(Base):
    __tablename__ = 'job_listings'
    id = Column(Integer, primary_key=True, autoincrement=True)
    company = Column(String(255))
    functions = Column(String(255))
    sectors = Column(String(255))
    employment_type = Column(String(255))
    criteria_url = Column(Text)
    date_posted = Column(String(255))
    location = Column(String(255))
    title = Column(String(255))
    listing_url = Column(Text)
    created_at = Column(DateTime, default=datetime.datetime.now)
