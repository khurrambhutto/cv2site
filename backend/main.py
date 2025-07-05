from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import pdf_parser
import portfolio_generator

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:3001", "http://localhost:3002"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload-pdf/")
async def create_upload_file(file: UploadFile = File(...)):
    pdf_content = await file.read()
    json_data = pdf_parser.parse_pdf(pdf_content)
    html_content = portfolio_generator.generate_portfolio(json_data)
    return HTMLResponse(content=html_content, status_code=200)
