# TS Validator using Open AI


## Introduction
This FastAPI application is designed to provide a robust and scalable API for validating .ts files.


## Installation

### Prerequisites
- Python 3.10+
- Git
- Virtualenv

### Steps
1. **Clone the repository**
    ```bash
    git clone https://github.com/farman99ahmed/ts-validator.git
    cd src
    ```

2. **Create a virtual environment**
    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment**

    - **On Windows**
        ```bash
        venv\Scripts\activate
        ```

    - **On macOS and Linux**
        ```bash
        source venv/bin/activate
        ```

4. **Install the required packages**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration
This application uses environment variables for configuration. Export following variables

```bash
export OPEN_AI_API_KEY="OPEN AI API KEY"
export OPEN_AI_MODEL="OPEN AI MODEL NAME"
```

## Running the Application
To run the application, use the following command:

```bash
uvicorn server:app --reload
```

This will start the server at http://localhost:8000 by default.
You can access swagger docs at http://localhost:8000/docs
