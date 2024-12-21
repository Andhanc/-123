FROM python:3.12

# Set the working directory inside the container
WORKDIR /backend

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the application code
COPY . .

EXPOSE 5000

CMD ["gunicorn", "-b", ":5000", "server:app"]
