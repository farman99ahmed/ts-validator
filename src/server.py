"""
FastAPI Server Module

This module initializes and runs the FastAPI application.

Usage:
1. Start the server:
    - Use an ASGI server like uvicorn:
        uvicorn server:app --reload

Endpoints:
- /health: Endpoint to get health of application
- /validate: Endpoint to validate `.ts` file

"""

import uuid
import logging
from fastapi import FastAPI, UploadFile, BackgroundTasks
from fastapi.responses import FileResponse
from config import AppSettings
from application import make_open_ai_request
from utils import check_and_delete_file_if_exists

config = AppSettings()

app = FastAPI(
    title = config.TITLE
)

# Set logging config
logging.basicConfig(format = f'{config.TITLE} - [%(asctime)s] [%(levelname)s] : %(message)s', level = logging.INFO)

@app.get("/health")
async def health():
    """Endpoint to return health of the application"""
    return {"message": f"{config.TITLE} is healthy."}

@app.post("/validate")
async def validate(file: UploadFile, bg_task: BackgroundTasks):
    """Endpoint to validate `.ts` file"""
    try:
        # Read file
        logging.info(f"Reading file")
        ts_file = file.file.read().decode("utf-8")
        # Create sample output file
        output_file = f"{uuid.uuid4()}.ts"
        # Open AI inference
        response = await make_open_ai_request(ts_data=ts_file)
        # Write response back in file
        with open(output_file, 'w', encoding='UTF-8') as op_file:
            op_file.write(response)
        # Delete response file from machine after returning the file
        bg_task.add_task(check_and_delete_file_if_exists, output_file)
        # Return output file
        return FileResponse(output_file, background=bg_task)
    except Exception as e:
        error_stack = {
            "type": type(e).__name__,
            "file": __file__,
            "line": e.__traceback__.tb_lineno,
            "message": str(e)
        }
        logging.error(error_stack)
        return {"error": f"There was an error processing you request. {str(e)}"}
