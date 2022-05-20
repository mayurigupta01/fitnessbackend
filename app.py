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


@app.route('/calculate_daily_calorie', methods=['POST'])
def calculate_daily_calorie():
    try:
        if request.method == 'POST':
            caloricNeed = 0

            request_data = request.get_json()
            gender = request_data['genderValue']
            weight = request_data['weightValue']
            heightFeet = request_data['heightFeetValue']
            heightInches = request_data['heightInchesValue']
            age = request_data['ageValue']
            activityLevel = request_data['activityLevelValue']

            if(gender == "male"):
                caloricNeed = (66 + (6.2 * weight) + (12.7 * ((heightFeet * 12) + heightInches)) - (6.76 * age)) * activityLevel
            elif(gender == "female"):
                caloricNeed = (655 + (4.35 * weight) + (4.7 * ((heightFeet * 12) + heightInches)) - (4.7 * age)) * activityLevel
            
            return jsonify({"caloricNeed": caloricNeed}), 200
    except Error as e:
        return {"message": e.message}, 400
    else:
        return "Daily Caloric Need API"


if __name__ == '__main__':
    app.run()
