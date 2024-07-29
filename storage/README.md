# 📂 Info Design Document

## 📄 Description

The `storage` directory primarily contains the `abstract.py` file, which defines an abstract class for storage adapters. This abstract class outlines the necessary functionality that any storage class inheriting from it must implement.

### 📂 Directory Structure

- `storage/`
  - `abstract.py`
  - `mysql/`
    - `adapter.py`
  - `sql/`
    - `adapter.py`

### 📝 `abstract.py`

The `abstract.py` file contains an abstract base class that storage adapters must inherit from. This ensures that all storage adapters implement a consistent set of methods, facilitating uniform interaction with different database systems.

### 🗂️ Subdirectories

1. **`mysql/`**: Contains an adapter for the MySQL database.
   - **Usage**: Primary use case.
   - **Details**: Utilizes SQLAlchemy to interact with the MySQL database.
   - **Files**:
     - `adapter.py`: Implements the MySQL adapter logic.

2. **`sql/`**: Contains an adapter for the SQLite database.
   - **Usage**: Not recommended for production.
   - **Details**: Utilizes SQLAlchemy to interact with the SQLite database.
   - **Files**:
     - `adapter.py`: Implements the SQLite adapter logic.

### 🔄 Summary

By maintaining a clear directory structure and utilizing an abstract base class, the `storage` module ensures consistent and scalable interactions with different database systems. This design allows for easy extension and integration of additional database adapters in the future.

---

This design document provides an organized overview of the `storage` directory, highlighting the abstract class's role and detailing the specific subdirectories for different database adapters.