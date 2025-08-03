import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import joblib

# Load data
data = pd.read_csv('diabetes_data.csv')

# Encode 'Outcome' column (Yes = 1, No = 0)222222
outcome_names = data['Outcome'].unique()
outcome_map = {name: i for i, name in enumerate(outcome_names)}
data['Outcome_encoded'] = data['Outcome'].map(outcome_map)

# Select features and label
X = data[['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
          'BMI', 'DiabetesPedigreeFunction', 'Age']]
y = data['Outcome_encoded']

# Train KNN model
model = KNeighborsClassifier(n_neighbors=3)
model.fit(X, y)

# Save model and mapping
joblib.dump(model, 'model.pkl')
joblib.dump(outcome_map, 'outcome_map.pkl')

print('KNN model and outcome mapping saved successfully.')
