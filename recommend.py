import random

# Mock data for doctors and labs
DOCTORS = [
    {"id": 1, "name": "Dr. John Smith", "specialization": "Cardiology", "location": "New York"},
    {"id": 2, "name": "Dr. Alice Johnson", "specialization": "Dermatology", "location": "Los Angeles"},
    {"id": 3, "name": "Dr. Mark Lee", "specialization": "Neurology", "location": "San Francisco"}
]

LABS = [
    {"id": 1, "name": "HealthTest Lab", "tests_available": ["Blood Test", "X-ray"], "location": "New York"},
    {"id": 2, "name": "QuickLabs", "tests_available": ["Blood Test", "MRI"], "location": "San Francisco"},
    {"id": 3, "name": "MediTest Labs", "tests_available": ["CT Scan", "X-ray"], "location": "Los Angeles"}
]

class PatientAgent:
    def __init__(self, patient_id, symptoms, location):
        self.patient_id = patient_id
        self.symptoms = symptoms
        self.location = location

    def get_patient_needs(self):
        return self.symptoms, self.location

    def recommend(self):
        # Simulate interaction with the doctor and lab agents to recommend
        recommended_doctor = self._recommend_doctor()
        recommended_lab = self._recommend_lab()

        return recommended_doctor, recommended_lab

    def _recommend_doctor(self):
        # For simplicity, choose a doctor with a matching specialization
        possible_doctors = [doctor for doctor in DOCTORS if doctor['specialization'].lower() in [symptom.lower() for symptom in self.symptoms]]
        if possible_doctors:
            return random.choice(possible_doctors)
        return None

    def _recommend_lab(self):
        # Choose a lab based on location and available tests
        possible_labs = [lab for lab in LABS if lab['location'].lower() == self.location.lower()]
        if possible_labs:
            return random.choice(possible_labs)
        return None


# Simulating communication with Fetch.ai agents (mocking the agent communication part)
class RecommenderAgent:
    def __init__(self, patient_agent):
        self.patient_agent = patient_agent

    def get_recommendations(self):
        # Get patient needs
        symptoms, location = self.patient_agent.get_patient_needs()
        
        # Use the recommender logic to suggest doctor and lab
        doctor, lab = self.patient_agent.recommend()
        
        return doctor, lab
