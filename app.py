from flask import Flask, render_template

app = Flask(__name__)

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