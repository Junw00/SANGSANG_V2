from flask import Flask
import json

import random

app = Flask(__name__)

with open('config.json', 'r') as f:
    json_data = json.load(f)


@app.route('/verify',  methods=['POST'])
def summary():
    
    random_id = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
    json_data['id'] = random_id

    print(json_data)
    response = app.response_class(
        response=json.dumps(json_data),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    app.run()
