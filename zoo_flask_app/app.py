from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load trained ML model
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
    feature_names = [
        'hair','feathers','eggs','milk','airborne',
        'aquatic','predator','toothed','backbone',
        'breathes','venomous','fins','tail',
        'domestic','catsize'
    ]

    features = [int(request.form.get(f, 0)) for f in feature_names]

    prediction_num = model.predict([features])[0]
    prediction_label = CLASS_MAP.get(prediction_num, "Unknown")

    return render_template(
        "index.html",
        popup_message=f"🐾 Predicted Animal Class: {prediction_label}"
    )

if __name__ == "__main__":
    app.run(debug=True)
