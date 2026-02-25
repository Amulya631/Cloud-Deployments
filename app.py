from flask import Flask, request, jsonify

app = Flask(__name__)

# Level 1 Robot
@app.route("/")
def hello():
    return "Hi 👋 I'm now a Helper Robot!"

# Level 2 Feature 1
# Calculator Robot
@app.route("/add", methods=["POST"])
def add_numbers():

    data = request.json

    num1 = data["num1"]
    num2 = data["num2"]

    result = num1 + num2

    return jsonify({
        "result": result
    })


# Level 2 Feature 2
# BMI Calculator
@app.route("/bmi", methods=["POST"])
def bmi():

    data = request.json

    weight = data["weight"]
    height = data["height"] / 100

    bmi_value = weight / (height * height)

    return jsonify({
        "BMI": round(bmi_value,2)
    })


# Level 2 Feature 3
# Form validation

@app.route("/register", methods=["POST"])
def register():

    data = request.json

    age = data["age"]

    if age < 0:

        return jsonify({
            "error": "Invalid age"
        })

    return jsonify({
        "message": "Registration successful"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
