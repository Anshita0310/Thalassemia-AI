from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

# Database config
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'data.db')
db = SQLAlchemy(app)

# Models
class Donor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    blood_type = db.Column(db.String(5))
    location = db.Column(db.String(200))

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    blood_type = db.Column(db.String(5))
    location = db.Column(db.String(200))

with app.app_context():
    db.create_all()


# Load model and encoders
model = joblib.load("model.pkl")
le_gender = joblib.load("le_gender.pkl")
le_symptoms = joblib.load("le_symptoms.pkl")
le_family = joblib.load("le_family.pkl")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    age = int(data['age'])
    gender = le_gender.transform([data['gender'].lower()])[0]
    symptoms = le_symptoms.transform([data['symptoms'].lower()])[0]
    family = le_family.transform([data['familyHistory'].lower()])[0]

    features = np.array([[age, gender, symptoms, family]])
    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][prediction]  # get confidence for predicted class

    # Save result (optional for charting later)
    with open("results_log.txt", "a") as log:
        log.write(f"{prediction}\n")

    if prediction == 1:
        return jsonify({
            "message": "High Risk - Genetic counseling recommended.",
            "confidence": round(probability * 100, 2)
        })
    else:
        return jsonify({
            "message": "Low Risk - No action needed now.",
            "confidence": round(probability * 100, 2)
        })


@app.route('/register_donor', methods=['POST'])
def register_donor():
    data = request.get_json()
    donor = Donor(name=data['name'], blood_type=data['blood_type'], location=data['location'])
    db.session.add(donor)
    db.session.commit()
    return jsonify({"message": "Donor registered successfully"})

@app.route('/register_patient', methods=['POST'])
def register_patient():
    data = request.get_json()
    patient = Patient(name=data['name'], blood_type=data['blood_type'], location=data['location'])
    db.session.add(patient)
    db.session.commit()
    return jsonify({"message": "Patient registered successfully"})

@app.route('/match_donors/<patient_id>', methods=['GET'])
def match_donors(patient_id):
    patient = Patient.query.get(patient_id)
    if not patient:
        return jsonify({"error": "Patient not found"}), 404

    matches = Donor.query.filter_by(blood_type=patient.blood_type).all()
    results = [{"id": d.id, "name": d.name, "location": d.location} for d in matches]

    return jsonify({"matches": results})

@app.route('/donors', methods=['GET'])
def get_donors():
    donors = Donor.query.all()
    result = [
        {"id": d.id, "name": d.name, "blood_type": d.blood_type, "location": d.location}
        for d in donors
    ]
    return jsonify(result)

@app.route('/patients', methods=['GET'])
def get_patients():
    patients = Patient.query.all()
    result = [
        {"id": p.id, "name": p.name, "blood_type": p.blood_type, "location": p.location}
        for p in patients
    ]
    return jsonify(result)

@app.route('/donor/<int:id>', methods=['DELETE', 'PUT'])
def modify_donor(id):
    donor = Donor.query.get_or_404(id)

    if request.method == 'DELETE':
        db.session.delete(donor)
        db.session.commit()
        return jsonify({"message": "Donor deleted successfully"})

    if request.method == 'PUT':
        data = request.get_json()
        donor.name = data['name']
        donor.blood_type = data['blood_type']
        donor.location = data['location']
        db.session.commit()
        return jsonify({"message": "Donor updated successfully"})

@app.route('/patient/<int:id>', methods=['DELETE', 'PUT'])
def modify_patient(id):
    patient = Patient.query.get_or_404(id)

    if request.method == 'DELETE':
        db.session.delete(patient)
        db.session.commit()
        return jsonify({"message": "Patient deleted successfully"})

    if request.method == 'PUT':
        data = request.get_json()
        patient.name = data['name']
        patient.blood_type = data['blood_type']
        patient.location = data['location']
        db.session.commit()
        return jsonify({"message": "Patient updated successfully"})

@app.route('/risk_stats', methods=['GET'])
def risk_stats():
    high = 0
    low = 0
    try:
        with open("results_log.txt", "r") as f:
            for line in f:
                if line.strip() == "1":
                    high += 1
                elif line.strip() == "0":
                    low += 1
    except FileNotFoundError:
        pass  # no file yet = 0 counts

    return jsonify({"high": high, "low": low})


if __name__ == '__main__':
    app.run(debug=True)
