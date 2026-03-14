from flask import Flask, render_template, request, jsonify
import joblib
import pandas as pd
import traceback

app = Flask(__name__)

# Load the trained model pipeline
try:
    model = joblib.load('model.joblib')
except Exception as e:
    print("Warning: Could not load model. Ensure train_model.py is run first.")
    model = None

# Recommendations based on prediction
RECOMMENDATIONS = {
    'Normal': "Your blood pressure indicators are in a healthy range. Continue maintaining a balanced diet, regular exercise, and a healthy lifestyle.",
    'Elevated': "Your indicators suggest elevated blood pressure. Consider reducing sodium intake, increasing physical activity, and monitoring your blood pressure regularly.",
    'Stage 1': "You are at risk for Stage 1 Hypertension. It is advisable to consult a healthcare provider for a formal assessment and adopt heart-healthy habits.",
    'Stage 2': "Your results indicate a high likelihood of Stage 2 Hypertension. Please seek medical advice promptly to discuss potential medication and lifestyle adjustments.",
    'Crisis': "URGENT: Your indicators suggest a possible Hypertensive Crisis. Seek immediate emergency medical attention."
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded.'}), 500

    try:
        data = request.json
        
        # Expected features matching the training data
        features = {
            'Age': [int(data.get('age', 0))],
            'Gender': [data.get('gender', 'Other')],
            'BMI': [float(data.get('bmi', 0.0))],
            'Heart_Rate': [float(data.get('heart_rate', 0.0))],
            'Total_Cholesterol': [float(data.get('cholesterol', 0.0))],
            'Exercise_Hours_Per_Week': [float(data.get('exercise', 0.0))],
            'Smoking_Status': [data.get('smoking', 'Never')],
            'Family_History_Hypertension': [data.get('family_history', 'No')]
        }
        
        df = pd.DataFrame(features)
        
        # Predict
        prediction = model.predict(df)[0]
        recommendation = RECOMMENDATIONS.get(prediction, "Consult a doctor for personalized advice.")
        
        return jsonify({
            'prediction': prediction,
            'recommendation': recommendation
        })
        
    except Exception as e:
        print("Error during prediction:")
        traceback.print_exc()
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True,port=8000)
