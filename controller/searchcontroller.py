from flask import Blueprint, request
from model.config import ConfigScrap
from core.scraper import getExecutor

search = Blueprint('search', __name__)

@search.route('/search', methods=['POST'])
def search_route():  # Renombra la función de vista
    type = request.form['type'] if 'type' in request.form else 'linkedin'
    keyword = request.form['keyword'] if 'keyword' in request.form else ''
    location = request.form['location'] if 'location' in request.form else 'Leon, Guanajuato'
    initial_page = int(request.form['initial_page']) if 'initial_page' in request.form else 1
    final_page = int(request.form['final_page']) if 'final_page' in request.form else 1
    profiles_to_search = request.form['profiles_to_search'] if 'profiles_to_search' in request.form else []
    is_search = request.form['is_search'] if 'is_search' in request.form else False

    conf = ConfigScrap(keyword=keyword, location=location, initial_page=initial_page, final_page=final_page,
                       profiles_to_search=profiles_to_search, is_search=is_search, type=type)
    
    print(f"conf: {conf.type}")
    
    executor = getExecutor(conf.type)
    
    print(f"is correct executor: {executor.is_ok}")

    match executor.is_ok:
        case True:
            return executor.value.execute()
        case False:
            print(executor.error_message)

    return "ok"
