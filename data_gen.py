import pandas as pd
import numpy as np

def generate_data(num_samples=5000):
    np.random.seed(42)

    ages = np.random.randint(18, 90, num_samples)
    genders = np.random.choice(['Male', 'Female', 'Other'], num_samples, p=[0.48, 0.48, 0.04])
    bmis = np.round(np.random.normal(28, 5, num_samples), 1)
    
    # Blood pressure logic based on age and BMI loosely
    systolic = np.zeros(num_samples)
    diastolic = np.zeros(num_samples)
    
    for i in range(num_samples):
        # Slightly increase base BP with age and BMI
        base_sys = 100 + (ages[i] * 0.3) + (bmis[i] * 0.8)
        base_dia = 65 + (ages[i] * 0.15) + (bmis[i] * 0.4)
        
        # Add random noise
        systolic[i] = np.random.normal(base_sys, 12)
        diastolic[i] = np.random.normal(base_dia, 8)
        
    heart_rates = np.round(np.random.normal(70 + (bmis - 25)*0.5, 10), 0)
    cholesterols = np.round(np.random.normal(180 + (ages*0.5) + (bmis*1.2), 30), 0)
    
    exercise_hours = np.round(np.clip(np.random.normal(3, 2), 0, 15), 1)
    smoking = np.random.choice(['Never', 'Former', 'Current'], num_samples, p=[0.6, 0.25, 0.15])
    family_history = np.random.choice(['Yes', 'No'], num_samples, p=[0.35, 0.65])

    # Assign target labels based roughly on ACC/AHA guidelines
    hypertension_stages = []
    for sys, dia in zip(systolic, diastolic):
        if sys < 120 and dia < 80:
            stage = 'Normal'
        elif 120 <= sys <= 129 and dia < 80:
            stage = 'Elevated'
        elif (130 <= sys <= 139) or (80 <= dia <= 89):
            stage = 'Stage 1'
        elif (sys >= 180) or (dia >= 120):
            stage = 'Crisis'
        else: # sys >= 140 or dia >= 90
            stage = 'Stage 2'
        hypertension_stages.append(stage)

    data = pd.DataFrame({
        'Age': ages,
        'Gender': genders,
        'BMI': bmis,
        'Heart_Rate': heart_rates,
        'Total_Cholesterol': cholesterols,
        'Exercise_Hours_Per_Week': exercise_hours,
        'Smoking_Status': smoking,
        'Family_History_Hypertension': family_history,
        'Hypertension_Stage': hypertension_stages
    })

    return data

if __name__ == '__main__':
    df = generate_data()
    df.to_csv('synthetic_bp_data.csv', index=False)
    print(f"Dataset 'synthetic_bp_data.csv' generated with {len(df)} records.")
    print("Class distribution:")
    print(df['Hypertension_Stage'].value_counts())
