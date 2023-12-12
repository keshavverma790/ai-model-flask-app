# We will use python:3.12.0 as the base image for building the Flask container
FROM python:3.12.0

# It specifies the working directory where the Docker container will run
WORKDIR /app

# Copying all the application files to the working directory
COPY . .

# Install all the dependencies required to run the Flask application
RUN pip install -r requirements.txt

# Copy the .env file into the container
COPY .env .env

# Set environment variable to use .env file
ENV DOTENV_PATH .env

# Download necessary NLTK packages
RUN python -m nltk.downloader punkt
RUN python -m nltk.downloader averaged_perceptron_tagger
RUN python -m nltk.downloader wordnet

# Expose the Docker container for the application to run on port 5000
EXPOSE 5000

# The command required to run the Dockerized application
CMD ["python", "app.py"]