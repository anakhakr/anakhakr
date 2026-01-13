from flask import Flask, request, jsonify
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

app = Flask(__name__)

model = tf.keras.models.load_model("sentiment_lstm_model.h5")

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

MAX_LEN = 100

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    text = data["text"]

    seq = tokenizer.texts_to_sequences([text])
    padded = pad_sequences(seq, maxlen=MAX_LEN)

    pred = model.predict(padded)
    sentiment = pred.argmax()

    labels = {0: "Negative", 1: "Neutral", 2: "Positive"}
    return jsonify({"sentiment": labels[sentiment]})

if __name__ == "__main__":
    app.run(debug=True)
