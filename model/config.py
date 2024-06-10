from dataclasses import dataclass,field
from typing import Optional,List


@dataclass
class Config:
    """
    clase para definir los parametros de busqueda

    params:
    keywords: str
    pages: Optional[int] = 1
    title: Optional[str] = "developer"
    location: Optional[str] = ""
    geo_urn: Optional[str] = ""
    """
    keywords  : str
    pages     : Optional[int] = 1
    title     : Optional[str] = "developer"
    location  : Optional[str] = ""
    geo_urn   : Optional[str] = ""


@dataclass
class ConfigScrap:
    """
    clase para definir los parametros de busqueda
    esto se hace para agregar valores por defecto
    y no tener que pasar todos los parametros
    """
    keyword  : Optional[str] = ""
    location  : Optional[str] = "Leon, Guanajuato"
    initial_page : Optional[int] = 1
    final_page   : Optional[int] = 1
    profiles_to_search : Optional[List[str]] = field(default_factory=list)
    is_search : Optional[bool] = False
    type: Optional[str] = "linkedin"


    def to_dict(self):
        return {
            "keyword": self.keyword,
            "location": self.location,
            "initial_page": self.initial_page,
            "final_page": self.final_page,
            "profiles_to_search": self.profiles_to_search,
            "is_search": self.is_search,
            "type": self.type
        }