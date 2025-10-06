# Use official Python 3 image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy your package and requirements
COPY . /app

# Install pip editable package
RUN pip install --upgrade pip \
    && pip install -e .

# Set the default command to launch Python CLI
CMD ["python3", "-m", "scientific_calculator.calc"]
