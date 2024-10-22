
# Vehicle Health Prediction

![Health-prediction-model](https://github.com/user-attachments/assets/719b4641-35d0-402e-bb81-3f58448943fd)

## Overview

The **Vehicle Health Prediction** project is a machine learning application that predicts the health status of vehicles based on various input features such as engine RPM, oil pressure, fuel pressure, and temperatures. This application aims to assist vehicle owners and technicians in diagnosing potential issues before they become severe, ultimately enhancing vehicle maintenance and safety.

## Features

- Predictive analysis of vehicle health based on real-time data inputs.
- User-friendly web interface built with Flask for easy interaction.
- REST API for receiving vehicle data and returning health predictions.
- Model training using Random Forest Classifier, ensuring reliable predictions.

## Technologies Used

- **Backend**: Flask
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: Pickle (for model persistence)
- **Containerization**: Docker

## Installation

### Prerequisites

- Python 3.x
- Pip (Python package manager)
- Docker (for containerization)

### Clone the repository

```bash
git clone https://github.com/CodingAksh/Vehicle-Health-Prediction-Model.git
cd vehicle-health-prediction
```

### Install dependencies

Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

Install required packages:

```bash
pip install -r requirements.txt
```

### Run the application

To run the Flask application locally, execute:

```bash
python app.py
```

Access the application at `http://localhost:5000`.

### Docker

To run the application using Docker, build the Docker image:

```bash
docker build -t vehicle-health-prediction .
```

Then run the Docker container:

```bash
docker run -p 5000:5000 vehicle-health-prediction
```

## Usage

1. Open the web application in your browser.
2. Input the required vehicle parameters in the form.
3. Click the "Predict" button to receive health status predictions.
