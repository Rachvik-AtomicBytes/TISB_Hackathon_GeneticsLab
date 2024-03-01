import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.multioutput import MultiOutputClassifier
from joblib import dump, load
from flask import Flask, render_template, request

# Load genetic information file
genetic_data = pd.read_csv('genet.csv', encoding='ISO-8859-1')

# Define target columns
target_columns = ['Genetic_mutation', 'Treatment_Plan', 'Chromosome_Involved']

# Feature selection
feature_columns = ['Genetic_Condition']

# Separate features and target
X = genetic_data[feature_columns]
y = genetic_data[target_columns]

# Encode target variables
label_encoders = {}
for column in y.columns:
    label_encoders[column] = LabelEncoder()
    y[column] = label_encoders[column].fit_transform(y[column])

# Handle string features using OneHotEncoder
string_encoder = OneHotEncoder(handle_unknown='ignore')  # Handle unknown categories
X_encoded = pd.DataFrame(string_encoder.fit_transform(X).toarray())

# Create a MultiOutputClassifier for multi-label prediction
clf = MultiOutputClassifier(RandomForestClassifier())
clf.fit(X_encoded, y)

# Save the string encoder for later use during prediction
dump(string_encoder, 'string_encoder.joblib')

# Create a Flask app for user input
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('IN.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Load the string encoder
        string_encoder = load('string_encoder.joblib')

        # Get user input from the form
        user_input = request.form['user_input']

        # Encode the user input
        user_input_encoded = pd.DataFrame(string_encoder.transform([[user_input]]).toarray())

        # Make predictions
        result = clf.predict(user_input_encoded)[0]

        # Decode results
        result_decoded = {column: label_encoders[column].inverse_transform([result[i]])[0] for i, column in enumerate(y.columns)}

        # Pass user input and results to the 'result.html' template
        return render_template('result.html', user_input=user_input, result=result_decoded)

if __name__ == '__main__':
    app.run(debug=True)