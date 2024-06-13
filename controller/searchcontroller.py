from flask import Blueprint, request
from model.config import ConfigScrap
from core.scraper import getExecutor
import json

search = Blueprint('search', __name__)

@search.route('/search', methods=['POST'])
def search_route():
    search_type = request.form.get('type', 'linkedin')
    keyword = request.form.get('keyword', '')
    location = request.form.get('location', 'Leon, Guanajuato')
    initial_page = int(request.form.get('initial_page', 1))
    final_page = int(request.form.get('final_page', 1))
    profiles_to_search = request.form.get('profiles_to_search', '[]')
    is_search = request.form.get('is_search', 'false').lower() == 'true'

    # Convert profiles_to_search to a list using json.loads for safety
    profiles_to_search = json.loads(profiles_to_search)

    conf = ConfigScrap(keyword=keyword, location=location, initial_page=initial_page, final_page=final_page,
                       profiles_to_search=profiles_to_search, is_search=is_search, type=search_type)
    
    print(f"ConfigScrap: {conf}")
    print(f"Type of profiles_to_search: {type(conf.profiles_to_search)}")
    
    #convertir conf.profiles_to_search a lista si es un string ese se ve como "['profile1','profile2']"
    if isinstance(conf.profiles_to_search, str):
        conf.profiles_to_search = conf.profiles_to_search.replace("[","").replace("]","").replace("'","").split(",")

    #imprimir el tipo de profiles_to_search
    print(f"Type of profiles_to_search: {type(conf.profiles_to_search)}")

    executor = getExecutor(conf.type)
    
    print(f"is correct executor: {executor.is_ok}")

    if executor.is_ok:
        result = executor.value.execute(conf)
        if result:
            return {
                "status": "ok",
                "data": result
            }
    else:
        return {
            "status": "error",
            "message": "Invalid executor type"
        }
    
    return {
        "status": "error",
        "message": "An error occurred"
    }


