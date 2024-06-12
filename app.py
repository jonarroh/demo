from flask import Flask, jsonify, request
from flask_cors import CORS
import core.scraper as scraper
import model.config as config
from controller.searchcontroller import search
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# app.register_blueprint(search)

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
    

is_production = os.environ.get('isDev')

if __name__ == "__main__":
  if is_production:
    app.run(host='0.0.0.0', port=5000)
  else:
    app.run(host='0.0.0.0', port=5000, debug=True)

