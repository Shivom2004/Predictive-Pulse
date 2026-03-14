
Predictive Pulse: Harnessing Machine Learning for Blood Pressure Analysis
 Project Overview
Predictive Pulse is a machine learning–based web application designed to predict and analyze blood pressure levels. The system uses health-related data and applies machine learning algorithms to classify the stage of hypertension.

The application is developed using Python and Flask for the backend and HTML, CSS, and JavaScript for the frontend.

Objectives
Predict blood pressure status using machine learning.

Assist in early detection of hypertension.

Provide a simple web interface for user input and prediction results.

Technologies Used

Python

Flask

Scikit-learn

Pandas

NumPy

Joblib

HTML

CSS

JavaScript

 Project Structure

Predictive_Pulse/
│
├── app.py
├── model_training.py
├── model.joblib
├── hypertension_dataset.csv
│
├── templates/
│   ├── index.html
│   └── result.html
│
└── static/
    └── style.css
⚙ Installation Steps
Clone the repository


git clone https://github.com/yourusername/Predictive-Pulse.git
Navigate to the project folder


cd Predictive-Pulse
Install required libraries


pip install flask pandas numpy scikit-learn joblib
Run the application


python app.py
Open in browser


http://127.0.0.1:5000
 Features
User-friendly interface

Machine learning based prediction

Real-time results

Health data analysis

📊 Dataset
The dataset used in this project contains patient health parameters such as age, blood pressure levels, and other health indicators used to predict hypertension.

👨‍💻 Author
Shivom Singh

📜 License
This project is developed for educational and academic purposes.
