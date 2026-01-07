# 1. Use an official Python image
FROM python:3.11-slim

# 2. Set the folder inside the container where our code will live
WORKDIR /code

# 3. Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy all our project files into the container
COPY . .

# 5. The command to start the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]