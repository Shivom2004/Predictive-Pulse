import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, classification_report

def train():
    try:
        df = pd.read_csv('synthetic_bp_data.csv')
    except Exception as e:
        print(f"Error reading dataset: {e}")
        return

    X = df.drop('Hypertension_Stage', axis=1)
    y = df['Hypertension_Stage']

    categorical_cols = ['Gender', 'Smoking_Status', 'Family_History_Hypertension']
    numerical_cols = ['Age', 'BMI', 'Heart_Rate', 'Total_Cholesterol', 'Exercise_Hours_Per_Week']

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', StandardScaler(), numerical_cols),
            ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_cols)
        ])

    # We use a Pipeline to encapsulate both preprocessing and the model
    model = Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42))
    ])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

    print("Training model...")
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)

    print(f"Validation Accuracy: {acc:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    joblib.dump(model, 'model.joblib')
    print("Model pipeline saved to model.joblib successfully.")

if __name__ == '__main__':
    train()
