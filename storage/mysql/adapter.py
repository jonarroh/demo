from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from storage.abstract import DB
import os
Base = declarative_base()

class MySQLAdapter(DB):
    def __init__(self, database_url=None):
        if database_url is None:
            database_url = os.getenv('DATABASE_URL')
        self.engine = create_engine(database_url)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def connect(self, database_url=None):
        if database_url is None:
            database_url = os.getenv('DATABASE_URL')
        self.engine = create_engine(database_url)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        Base.metadata.create_all(self.engine)
        self.session = self.Session()

    def execute(self, query, *args, **kwargs):
        result = self.session.execute(query, *args, **kwargs)
        return result

    def fetch(self, query, *args, **kwargs):
        result = self.session.execute(query, *args, **kwargs).fetchall()
        return result

    def close(self):
        self.session.close()

    def commit(self):
        self.session.commit()

    def rollback(self):
        self.session.rollback()

    def fetchAll(self, query, *args, **kwargs):
        return self.session.execute(query, *args, **kwargs).fetchall()

    def fetchOne(self, query, *args, **kwargs):
        return self.session.execute(query, *args, **kwargs).fetchone()

    def fetchMany(self, query, size, *args, **kwargs):
        return self.session.execute(query, *args, **kwargs).fetchmany(size)

    def saveAll(self, instances):
        self.session.add_all(instances)
        self.commit()

    def saveMany(self, instances):
        self.saveAll(instances)

    def saveOne(self, instance):
        self.session.add(instance)
        self.commit()

    def updateAll(self, instances):
        for instance in instances:
            self.session.merge(instance)
        self.commit()

    def updateMany(self, instances):
        self.updateAll(instances)

    def deleteAll(self, instances):
        for instance in instances:
            self.session.delete(instance)
        self.commit()
    
    def deleteMany(self, instances):
        self.deleteAll(instances)
    
    def deleteOne(self, instance):
        self.session.delete(instance)
        self.commit()

    def updateOne(self, instance):
        self.session.merge(instance)
        self.commit()

    