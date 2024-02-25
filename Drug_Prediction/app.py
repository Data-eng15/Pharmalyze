from flask import Flask, render_template, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

app = Flask(__name__)

# Load the dataset from CSV
data = pd.read_csv('F:\Machine Learning Project\Classification Problem\Drug_Prediction\drug200.csv')

# Split features (X) and target variable (y)
X = data[['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K']]
y = data['Drug']

# Convert categorical variables to numerical using one-hot encoding
X = pd.get_dummies(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize Naive Bayes classifier
clf = GaussianNB()

# Train the classifier
clf.fit(X_train, y_train)

# Define a function to preprocess input features
def preprocess_input(input_features):
    input_df = pd.DataFrame([input_features], columns=['Age', 'Sex', 'BP', 'Cholesterol', 'Na_to_K'])
    input_df['Sex'] = input_df['Sex'].map({'M': 1, 'F': 0})  # Convert 'Sex' to numerical values
    input_df = pd.get_dummies(input_df, columns=['BP', 'Cholesterol'])  # One-hot encode categorical variables
    input_df['Cholesterol_LOW'] = 0  # Add missing 'Cholesterol_LOW' column
    input_df = input_df.reindex(columns=X_train.columns, fill_value=0)  # Reorder columns to match X_train
    return input_df

# Define a function to predict drug
def predict_drug(input_features):
    input_df = preprocess_input(input_features)
    prediction = clf.predict(input_df)
    return prediction[0]  # Return the predicted drug label

# Route for the landing page
@app.route('/')
def index():
    return render_template('index.html')

# Route for drug prediction
@app.route('/predict', methods=['POST'])
def predict():
    age = int(request.form['age'])
    sex = request.form['sex']
    bp = request.form['bp']
    cholesterol = request.form['cholesterol']
    na_to_k = float(request.form['na_to_k'])
    
    # Check if age and Na_to_K are non-negative
    if age < 0 or na_to_k < 0:
        return render_template('error.html', message='Age and Na_to_K should not be negative')
    
    # Predict the drug based on user input
    input_features = [age, sex, bp, cholesterol, na_to_k]
    predicted_drug = predict_drug(input_features)

    # Render the prediction result template with the predicted drug
    return render_template('result.html', drug=predicted_drug)

if __name__ == '__main__':
    app.run(debug=True)
