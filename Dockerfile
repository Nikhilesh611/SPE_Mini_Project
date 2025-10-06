# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy dependency files
COPY pyproject.toml setup.cfg README.md ./

# Install build tools
RUN pip install --upgrade pip setuptools wheel

# Install the package in editable mode
RUN pip install --editable .[dev] --no-cache-dir

# Copy the rest of the code
COPY scientific_calculator/ ./scientific_calculator/

# Expose port 9090
EXPOSE 9090

# Run FastAPI app
CMD ["uvicorn", "scientific_calculator.api:app", "--host", "0.0.0.0", "--port", "9090"]
