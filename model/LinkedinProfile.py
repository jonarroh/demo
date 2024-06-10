from sqlalchemy import Column, String, Text, JSON, Integer
from sqlalchemy.ext.declarative import declarative_base


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