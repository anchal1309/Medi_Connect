from flask import Flask, render_template,jsonify, request
from recommend import PatientAgent, RecommenderAgent

app = Flask(__name__)

@app.route('/recommend', methods=['POST'])
def recommend():
    # Simulate patient data coming from a frontend (e.g., symptoms, location)
    data = request.json
    patient_symptoms = data.get("symptoms", [])
    patient_location = data.get("location", "")
    
    # Create a patient agent based on this data
    patient_agent = PatientAgent(patient_id=1, symptoms=patient_symptoms, location=patient_location)
    
    # Create the recommender agent and get recommendations
    recommender_agent = RecommenderAgent(patient_agent)
    recommended_doctor, recommended_lab = recommender_agent.get_recommendations()
    
    if recommended_doctor and recommended_lab:
        return jsonify({
            "doctor": recommended_doctor,
            "lab": recommended_lab
        }), 200
    else:
        return jsonify({
            "message": "No suitable doctor or lab found"
        }), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login_patient')
def login_patient():
    return render_template('login_patient.html')

@app.route('/login_lab')
def login_lab():
    return render_template('login_lab.html')

@app.route('/patient')
def patient():
    return render_template('patient.html')

@app.route('/login_doctor')
def login_doctor():
    return render_template('login_doctor.html')

@app.route('/lab')
def lab():
    return render_template('lab.html')

@app.route('/doctor')
def doctor():
    return render_template('doctor.html')

if __name__ == '__main__':
    app.run(debug=True,port =8000)