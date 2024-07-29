# 📂 Core Design Document

## 📄 Description

The `core` directory houses the various cores available for use in the project. Each core is responsible for executing specific tasks based on its unique logic.

### 🗂️ Directory Structure

- `core/`
  - `linkedin/`
    - `init.py`
    - `core.py`
  - `api/`
    - `init.py`
    - `core.py`
  - `job/`
    - `init.py`
    - `core.py`

### 🛠️ Adding a New Core

To add a new core to the project, follow these steps:

1. **Update the Executor Mapping**:
   - Add the name of the core and an instance of the core class to the `EXECUTOR_MAPPING` dictionary.

    ```python
    EXECUTOR_MAPPING = {
        "linkedin": LinkedInExecutor(),
        "api": APIExecutor(),
        "job": JobExecutor()
    }
    ```

2. **Create Core Folder**:
   - Create a folder with the name of the new core inside the `core` directory.
   - Inside this folder, create two files: `init.py` and `core.py`.

3. **Implement Core Logic**:
   - In `core.py`, implement the business logic specific to the core.

4. **Initialize Core**:
   - In `init.py`, create a class that inherits from `Executor` and implements the `execute` method.

    ```python
    class LinkedInExecutor(Executor):
        def execute(self, *args, **kwargs):
            pass
    ```

## 📄 `core.py`

The `core.py` file within each core's directory should contain all the business logic pertinent to that core. This design ensures that the core logic is modular and easy to manage.

## 🔄 Summary

By adhering to this structure, new core types can be seamlessly integrated into the project, enhancing scalability and maintainability.

---

This design document provides a clear, step-by-step guide for adding new cores to the project, ensuring consistency and ease of development.