from flask import Flask
import json


app = Flask(__name__)

with open('config.json', 'r') as f:
    json_data = json.load(f)


@app.route('/verify',  methods=['POST'])
def summary():
    response = app.response_class(
        response=json.dumps(json_data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run()
