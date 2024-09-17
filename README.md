# Product API

This project is a **Flask-based REST API** for managing products, built with adherence to the **SOLID principles**. 

## Features

- **Create a Product**: POST `/api/products`
- **Retrieve a Product**: GET `/api/products/<id>`

## Installation

### Prerequisites

- **Docker**

### Steps

1. **Build the Docker image**:

```bash
docker build -t product-api .
```

2. **Run the Docker container**:

```bash
docker run -d -p 5000:5000 product-api
```

3. **Check the API**:

The API will be running at `http://localhost:5000`.

### API Endpoints

- **Create a Product**:
    ```bash
    POST /api/products
    ```
    Example:
    ```bash
    curl -X POST http://localhost:5000/api/products -H "Content-Type: application/json" -d '{"name": "Laptop", "price": 1500, "description": "A high-end gaming laptop"}'
    ```

- **Get a Product by ID**:
    ```bash
    GET /api/products/<id>
    ```
    Example:
    ```bash
    curl http://localhost:5000/api/products/1
    ```

## Running Tests

1. **Install Dependencies**:

```bash
pip install -r requirements.txt
```

2. **Run Tests**:

```bash
pytest tests/test_product.py
```

This will run unit tests for the product API.

## Technologies

- **Python 3.10**
- **Flask**
- **Docker**
- **pytest**
