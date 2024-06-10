from abc import ABC, abstractmethod




class DB(ABC):
    @abstractmethod
    def connect(self, *args, **kwargs):
        pass

    @abstractmethod
    def execute(self, *args, **kwargs):
        pass

    @abstractmethod
    def fetch(self, *args, **kwargs):
        pass

    @abstractmethod
    def close(self, *args, **kwargs):
        pass

    @abstractmethod
    def commit(self, *args, **kwargs):
        pass

    @abstractmethod
    def rollback(self, *args, **kwargs):
        pass

    @abstractmethod
    def fetchAll(self, *args, **kwargs):
        pass

    @abstractmethod
    def fetchOne(self, *args, **kwargs):
        pass

    @abstractmethod
    def fetchMany(self, *args, **kwargs):
        pass

    @abstractmethod
    def saveAll(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def saveMany(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def saveOne(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def updateAll(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def updateMany(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def updateOne(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def deleteAll(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def deleteMany(self, *args, **kwargs):
        pass
    
    @abstractmethod
    def deleteOne(self, *args, **kwargs):
        pass
