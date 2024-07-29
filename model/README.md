# 📂 Model Design Document

## 📄 Description

The `model` directory contains class models and SQLAlchemy models. These models are used to interact with the database and to facilitate JSON encoding/decoding. This directory is closely related to the `storage` and `db` directories.

### 🗂️ Directory Structure

- `model/`
  - `user.py`
  - `product.py`
  - `order.py`
  - ...

### 📝 Python Data Class Example

Using `dataclass` to define a simple data structure for encoding and decoding JSON:

```python
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class ConfigScrap:
    """
    Class to define search parameters.
    This is done to add default values and avoid passing all parameters.
    """
    keyword: Optional[str] = ""
    location: Optional[str] = "Leon, Guanajuato"
    initial_page: Optional[int] = 1
    final_page: Optional[int] = 1
    profiles_to_search: Optional[List[str]] = field(default_factory=list)
    is_search: Optional[bool] = False
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
```

### 📝 SQLAlchemy Class Example

Using SQLAlchemy to define a more detailed and functional user model:

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
```

### 🔗 Useful Links

- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLAlchemy ORM](https://docs.sqlalchemy.org/en/14/orm/index.html)
- [SQLAlchemy ORM Tutorial](https://docs.sqlalchemy.org/en/14/orm/tutorial.html)

### 🔄 Summary

The `model` directory is essential for defining the structure of the data and ensuring consistent interaction with the database. By using Python dataclasses for easy JSON encoding/decoding and SQLAlchemy models for database operations, the project maintains flexibility and leverages the power of SQLAlchemy for complex database interactions.

---

This design document provides a clear overview of the `model` directory, illustrating how to define both simple and complex models and offering useful resources for further learning.