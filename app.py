from flask import Flask, jsonify, request
from flask_cors import CORS

import core.scraper as scraper
import model.config as config

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

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
    

app.run(debug=True)
