from core.api.index import APIExecutor
from core.linkedln.index import LinkedInExecutor
from utils.Result import Result

# Mapping of executor type to executor instance
EXECUTOR_MAPPING = {
    "linkedin": LinkedInExecutor(),
    "api": APIExecutor()
}

"""
This function returns an executor instance based on the type provided.
"""
def getExecutor(type: str) -> Result:
    executor_instance = EXECUTOR_MAPPING.get(type)
    if executor_instance:
        return Result().ok(executor_instance)
    else:
        return Result().err("Invalid executor type")
