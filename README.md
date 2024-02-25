# Pharmalyze

Pharmalyze is a web application that predicts the most suitable drug based on user input features using the Naive Bayes algorithm. It provides a user-friendly interface for drug prediction and is built using the Flask framework for backend development and HTML/CSS for the user interface.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Usage](#usage)

## Features

- **Drug Prediction**: Pharmalyze predicts the most suitable drug for a patient based on input features such as age, sex, blood pressure, cholesterol level, and Na_to_K ratio.
- **Naive Bayes Algorithm**: The application employs the Naive Bayes algorithm, a popular machine learning technique for classification tasks, to predict the appropriate drug class.
- **Modern UI**: Pharmalyze features a modern and intuitive user interface designed using HTML and CSS, providing a seamless user experience for drug prediction.
- **Docker Image**: The application is dockerized for easy deployment and scalability. It allows the application to be run in containerized environments with minimal setup.

## Technologies Used

Pharmalyze is built using the following technologies:

- **Python**: Python is used as the primary programming language for backend development and implementing the Naive Bayes algorithm.
- **Flask**: Flask, a lightweight WSGI web application framework, is used for building the backend server and handling HTTP requests.
- **HTML/CSS**: HTML is used for structuring the web pages, while CSS is used for styling and enhancing the visual appearance of the user interface.
- **Docker**: Docker is used for containerization, allowing the application to be packaged with its dependencies and run consistently across different environments.

## Usage

Follow these steps to use Pharmalyze:

1. **Clone the Repository**: Clone the Pharmalyze repository to your local machine using the following command:

   ```bash
   git clone https://github.com/your_username/pharmalyze.git
2. Navigate to the Project Directory: Change your current directory to the cloned Pharmalyze repository:
cd pharmalyze
3.Build the Docker Image: Build the Docker image for Pharmalyze using the provided Dockerfile:
docker build -t pharmalyze .
4. Run the Docker Container: Run the Docker container for Pharmalyze, exposing it on port 5000:
docker run -d -p 5000:5000 pharmalyze
5. Access the Application: Access the Pharmalyze application in your web browser by navigating to the following URL:
http://localhost:5000

Feel free to customize the README.md file further to include additional information or sections as needed. Additionally, you may want to include screenshots of your application or additional usage instructions.
