import pdfplumber
import json
import os
import io
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import List, Optional

# Load environment variables from .env file
load_dotenv()

# Pydantic model for a single project
class Project(BaseModel):
    name: str = Field(description="The name of the project.")
    technologies: List[str] = Field(description="A list of technologies used in the project.")
    description: List[str] = Field(description="A list of bullet points describing the project.")

# Pydantic model for a single experience entry
class Experience(BaseModel):
    job_title: str = Field(description="The job title.")
    company: str = Field(description="The company name.")
    location: Optional[str] = Field(description="The location of the company.")
    dates: str = Field(description="The dates of employment.")
    description: List[str] = Field(description="A list of responsibilities and achievements.")

# Pydantic model for a single certification
class Certification(BaseModel):
    name: str = Field(description="The name of the certification.")
    issuer: str = Field(description="The issuing organization.")
    date: Optional[str] = Field(description="The date the certification was awarded.")
    description: Optional[str] = Field(description="A brief description of the certification.")

# Pydantic model for the structured resume data
class Resume(BaseModel):
    name: Optional[str] = Field(description="The full name of the person.")
    contact_information: Optional[dict] = Field(description="Contact information, including email, phone, and address.")
    summary: Optional[str] = Field(description="A summary of the person's skills and experience.")
    experience: List[Experience] = Field(description="A list of work experiences.")
    education: List[dict] = Field(description="A list of educational qualifications, including degree, institution, and dates.")
    projects: List[Project] = Field(description="A list of projects.")
    certifications: List[Certification] = Field(description="A list of certifications.")
    skills: List[str] = Field(description="A list of skills.")


def get_gemini_api_key():
    """Retrieves the Gemini API key from environment variables."""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in .env file.")
    return api_key

def parse_resume_with_gemini(text: str, api_key: str) -> dict:
    """
    Uses a LangChain agent with the Gemini API to parse resume text.

    Args:
        text: The resume text to parse.
        api_key: The Gemini API key.

    Returns:
        A dictionary containing the structured resume data.
    """
    llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=api_key)
    
    parser = PydanticOutputParser(pydantic_object=Resume)

    prompt = PromptTemplate(
        template="Parse the following resume text and extract the information into a structured JSON format.\n{format_instructions}\n{resume_text}",
        input_variables=["resume_text"],
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    chain = prompt | llm | parser

    return chain.invoke({"resume_text": text})


def parse_pdf(pdf_content: bytes) -> dict:
    """
    Parses a PDF file from its content, extracts text, and returns structured data.

    Args:
        pdf_content (bytes): The content of the PDF file.

    Returns:
        A dictionary containing the structured resume data.
    """
    try:
        api_key = get_gemini_api_key()

        with pdfplumber.open(io.BytesIO(pdf_content)) as pdf:
            full_text = ""
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"

        structured_data = parse_resume_with_gemini(full_text, api_key)

        # Log the structured data before returning
        print("Structured data from Gemini:", structured_data)
        print("Type of structured data:", type(structured_data))

        # Convert Pydantic model to dict if it's a Resume object
        if hasattr(structured_data, 'model_dump'):
            return structured_data.model_dump()
        else:
            return structured_data

    except Exception as e:
        print(f"An error occurred during PDF parsing: {e}")
        return {}