from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def weight_prediction():
    if request.method == 'GET':
        return render_template("iris-prediction.html")
    elif request.method == 'POST':
        print(dict(request.form))
        weight_features = dict(request.form).values()
        weight_features = np.array([float(x) for x in weight_features])
        model, std_scaler = joblib.load("model-development/weight-prediction-using-linear-regression.pkl")
        weight_features = std_scaler.transform([weight_features])
        print(weight_features)
        result = model.predict(weight_features)
        return render_template('weight-prediction.html', result=result)
    else:
        return "Unsupported Request Method"


if __name__ == '__main__':
    app.run(port=5000, debug=True)