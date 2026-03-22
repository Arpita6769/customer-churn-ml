from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))
columns = pickle.load(open("columns.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        input_data = request.form.to_dict()

        # convert to float
        input_data = {k: float(v) for k, v in input_data.items()}

        # create full feature vector
        final_input = [0] * len(columns)

        for i, col in enumerate(columns):
            if col in input_data:
                final_input[i] = input_data[col]

        final_input = np.array(final_input).reshape(1, -1)

        prediction = model.predict(final_input)

        if prediction[0] == 1:
            output = "⚠️ Customer likely to churn"
        else:
            output = "✅ Customer likely to stay"

        return render_template("index.html", prediction_text=output)

    except Exception as e:
        return render_template("index.html", prediction_text=str(e))

if __name__ == "__main__":
    app.run(debug=True)