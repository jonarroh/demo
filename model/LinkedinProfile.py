from sqlalchemy import Column, Text, JSON, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime



Base = declarative_base()

class LinkedInProfile(Base):
    __tablename__ = 'linkedin_profiles'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(Text)
    nombre = Column(Text)
    img = Column(Text)
    description = Column(Text)
    empresa_actual = Column(Text)
    about = Column(Text)
    idiomas = Column(JSON)
    conocimientos_aptitudes = Column(JSON)
    educacion = Column(JSON)
    licencias_certificaciones = Column(JSON)
    search_at = Column(DateTime, default=datetime.now)