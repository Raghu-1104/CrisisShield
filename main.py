from flask import Flask, request, render_template
from predict import predict_disaster

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.form
    disaster_type = data.get("disaster_type")
    location = data.get("location")
    prediction = predict_disaster(disaster_type, location)
    return render_template("results.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
