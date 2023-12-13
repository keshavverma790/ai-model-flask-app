# AI Model Flask Application

This project implements a Flask-based API service that performs sentiment analysis on tweets using a [pre-trained machine learning model](https://github.com/keshavverma790/tweets_sentiment_analysis_ai_model/blob/main/ai-model.ipynb). Additionally, it includes user authentication APIs, integrates with MySQL to store model requests and results, and is containerized using Docker for streamlined deployment via Kubernetes.

## Features

- **Sentiment Analysis**: Utilizes a machine learning model to predict sentiment from tweets.
- **User Authentication**: Provides user registration and login functionalities using JWT (JSON Web Tokens).
- **MySQL Integration**: Stores AI model requests and their results in a MySQL database.
- **Containerization**: Docker containerization ensures portability and scalability.
- **Deployment**: Ready for deployment using Kubernetes for orchestration.

## Requirements

The application requires the following dependencies, listed in the `requirements.txt` file:
- cryptography
- Flask
- Flask-Bcrypt
- Flask-JWT
- Flask-JWT-Extended
- Flask-Migrate
- Flask-RESTful
- Flask-SQLAlchemy
- scikit-learn
- PyMySQL
- nltk
- python-dotenv
- PyJWT==2.2.0

## API Endpoints

- Sentiment Prediction: /model/predict/<string:newTweet>
- User Registration: /user/register
- User Login: /user/login

## Development Environment Setup

### Cloning the Repository

Clone this repository to your local machine using Git:

```bash
git clone https://github.com/your-username/ai-model-flask-app.git
cd ai-model-flask-app
```

### Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

### NLTK Setup

Download necessary NLTK packages:

```bash
python -m nltk.downloader punkt
python -m nltk.downloader averaged_perceptron_tagger
python -m nltk.downloader wordnet
```

### Set Up Environment Variables

Copy the .env.example file to create your own .env file:

```
# Flask App Configurations
FLASK_APP=app.py
FLASK_ENV=development

# Secret Key for Flask Session
SECRET_KEY=your_secret_key_here

# Database Configuration
DATABASE_URI=your_database_connection_string_here

# Paths to Model Files
VECTORIZER_PATH=path_to_vectorizer_model.pickle
LR_MODEL_PATH=path_to_LR_model.pickle
```

```bash
cp .env.example .env
```

Update the .env file with your specific configurations and credentials.

### Running the Flask Application

Start the Flask application in development mode:

```bash
flask run
```

Access the API endpoints at http://localhost:5000.

## Deployment

### Docker

Build the Docker image:

```bash
docker build -t ai-model-flask-app .
```

Run the Docker container:

```bash
docker run -p 5000:5000 ai-model-flask-app
```

## Kubernetes

Deploy to Kubernetes:

```bash
kubectl apply -f deployment.yaml
```

Access the service:

```bash
minikube service flask-app-service
```

## Contributing

1. Fork the repository.
2. Create a new branch (git checkout -b feature/awesome-feature).
3. Make your changes.
4. Commit your changes (git commit -am 'Add awesome feature').
5. Push to the branch (git push origin feature/awesome-feature).
6. Create a new Pull Request.
