#!/usr/bin/env python
# coding: utf-8

# 1. Import Libs and Set API Keys

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn
from pydantic import BaseModel # Ensure BaseModel is imported


load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')


# 2. Load GROQ Model

model = ChatGroq(model = 'gemma2-9b-it', api_key = os.environ['GROQ_API_KEY'])


# 3. Create Prompt Template

generic_template = "Convert the following into {language} language"
prompt = ChatPromptTemplate.from_messages(
[
    ("system",generic_template),
    ("user","{input}")

]

)


# 4. Output Parser

parser = StrOutputParser()


# 5. Chain the process

chain = prompt|model|parser

# Define the input model for your chain
class ChainInput(BaseModel):
    language: str


# chain.invoke({"language":"bengali"})


# 6. App Definition

app = FastAPI(title = "Langchain Server", version= 1.0, description= "Simple API Server using Langchani runnable interfaces")


# 7. Chain Routes

add_routes(
    app,
    chain.with_types(input_type=ChainInput),  # Use .with_types() here
    path = '/chain',

)


if __name__ == "__main__":
    import uvicorn
    # Assuming your script is named 'main.py'
    uvicorn.run("serve:app", host="127.0.0.1", port=8000, reload=True)