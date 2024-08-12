from flask import Flask, jsonify, request
from flask_cors import CORS
import core.scraper as scraper
import model.config as config
from controller.searchcontroller import search
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from flask_socketio import SocketIO, emit


load_dotenv()

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app, resources={r"/*": {"origins": "http://localhost:5500,https://qawp.app.metaphorce.mx "}})

app.register_blueprint(search)

@app.route('/ping', methods=['GET', 'POST'])
def ping():
  return "pong"

@app.route('/api/people', methods=['POST'])
def people():
  data = {
  'keywords': request.form['keywords'],
  'pages': int(request.form['pages']) if 'pages' in request.form and request.form['pages'] else 1,
  'title': request.form['title'] if 'title' in request.form and request.form['title'] else ""
  }

  conf = config.Config(keywords=data['keywords'], pages=data['pages'], title=data['title'])
  result = scraper.scrappProfiles(conf.__dict__)
  return jsonify(result.to_dict('records'))


import json
from core.scraper import getExecutor
from model.config import ConfigScrap

@socketio.on('search')
def handle_search(data):
    search_type = data.get('type', 'linkedin')
    keyword = data.get('keyword', '')
    location = data.get('location', 'Leon, Guanajuato')
    initial_page = int(data.get('initial_page', 1))
    final_page = int(data.get('final_page', 1))
    profiles_to_search = data.get('profiles_to_search', '[]')
    is_search = data.get('is_search', 'false').lower() == 'true'

    profiles_to_search = json.loads(profiles_to_search)

    conf = ConfigScrap(keyword=keyword, location=location, initial_page=initial_page, final_page=final_page,
                       profiles_to_search=profiles_to_search, is_search=is_search, type=search_type)
    
    print(f"ConfigScrap: {conf}")
    print(f"Type of profiles_to_search: {type(conf.profiles_to_search)}")
    
    if isinstance(conf.profiles_to_search, str):
        conf.profiles_to_search = conf.profiles_to_search.replace("[","").replace("]","").replace("'","").split(",")

    print(f"Type of profiles_to_search: {type(conf.profiles_to_search)}")

    executor = getExecutor(conf.type)
    
    print(f"is correct executor: {executor.is_ok}")

    if executor.is_ok:
        result = executor.value.execute(conf)
        print(f"result: {result}")
        if result:
            print("emitting search_response")
            emit('search_response', {
                "status": "ok",
                "data": result
            })
            return
    else:
        print("emitting search_response with error")
        emit('search_response', {
            "status": "error",
            "message": "Invalid executor type"
        })
        return
    print("emitting search_response with error")
    emit('search_response', {
        "status": "error",
        "message": "An error occurred"
    })






if __name__ == "__main__":
  app.run(host='0.0.0.0', port=5000, debug=True)
