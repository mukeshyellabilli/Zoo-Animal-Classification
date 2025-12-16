from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

model = joblib.load("zoo_model.pkl")

CLASS_MAP = {
    1: "Mammal",
    2: "Bird",
    3: "Reptile",
    4: "Fish",
    5: "Amphibian",
    6: "Insect",
    7: "Invertebrate"
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        int(request.form['hair']),
        int(request.form['feathers']),
        int(request.form['eggs']),
        int(request.form['milk']),
        int(request.form['airborne']),
        int(request.form['aquatic']),
        int(request.form['predator']),
        int(request.form['toothed']),
        int(request.form['backbone']),
        int(request.form['breathes']),
        int(request.form['venomous']),
        int(request.form['fins']),
        int(request.form['tail']),
        int(request.form['domestic']),
        int(request.form['catsize'])
    ]

    prediction_num = model.predict([features])[0]
    prediction_label = CLASS_MAP.get(prediction_num, "Unknown")

    return render_template(
        "index.html",
        popup_message=f"🐾 Predicted Animal Class: {prediction_label}"
    )

if __name__ == "__main__":
    app.run(debug=True)
