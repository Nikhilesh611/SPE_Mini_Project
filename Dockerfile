# Use official Python image
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Copy dependency files
COPY pyproject.toml setup.cfg README.md ./

# Copy the package and tests
COPY scientific_calculator/ ./scientific_calculator/
COPY tests/ ./tests/

# Upgrade pip
RUN pip install --upgrade pip

# Install your package in editable mode along with dependencies
RUN pip install -e . 

# Default command to run tests
CMD ["python3", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"]
