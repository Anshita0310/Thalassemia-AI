import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import joblib

# Create a dummy dataset
data = {
    "age": [20, 25, 30, 22, 35, 19, 28, 40],
    "gender": ["male", "female", "male", "female", "male", "female", "female", "male"],
    "symptoms": ["yes", "no", "yes", "no", "yes", "yes", "no", "no"],
    "familyHistory": ["yes", "no", "yes", "no", "yes", "yes", "no", "no"],
    "risk": [1, 0, 1, 0, 1, 1, 0, 0],  # 1 = high risk, 0 = low risk
}

df = pd.DataFrame(data)

# Encode categorical variables
le_gender = LabelEncoder()
le_symptoms = LabelEncoder()
le_family = LabelEncoder()

df['gender'] = le_gender.fit_transform(df['gender'])
df['symptoms'] = le_symptoms.fit_transform(df['symptoms'])
df['familyHistory'] = le_family.fit_transform(df['familyHistory'])

X = df[["age", "gender", "symptoms", "familyHistory"]]
y = df["risk"]

# Train the model
model = LogisticRegression()
model.fit(X, y)

# Save the model and encoders
joblib.dump(model, "model.pkl")
joblib.dump(le_gender, "le_gender.pkl")
joblib.dump(le_symptoms, "le_symptoms.pkl")
joblib.dump(le_family, "le_family.pkl")

print("Model trained and saved successfully.")
