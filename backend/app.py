from flask import Flask, jsonify, request
from flask_cors import CORS
from fraud_logic import detect_fraud
import os

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = "backend/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/check-fraud", methods=["POST"])
def check_fraud():
    file = request.files["file"]
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    report = detect_fraud(file_path)
    return jsonify(report)

if __name__ == "__main__":
    app.run(debug=True)
