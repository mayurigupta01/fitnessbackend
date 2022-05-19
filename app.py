from flask import Flask
from flask import request, jsonify
from aifc import Error

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello backend api for fitness app!'


@app.route('/bmi', methods=['POST'])
def calculate_bmi():  # put application's code here
    try:
        if request.method == 'POST':
            request_data = request.get_json()
            height = request_data['height']
            weight = request_data['weight']
            BMI = (weight / (height * height)) * 703
            return jsonify({"BMI": BMI}), 200
    except Error as e:
        return {"message": e.message}, 400
    else:
        return "welcome to Bmi calculation page"


if __name__ == '__main__':
    app.run()
