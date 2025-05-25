#!/usr/bin/env python
# coding: utf-8

# 1. Import Libs and Set API Keys

# In[17]:


import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import uvicorn

load_dotenv()

os.environ['GOOGLE_API_KEY'] = os.getenv('GOOGLE_API_KEY')
os.environ['LANGCHAIN_API_KEY'] = os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2'] = "true"
os.environ['LANGCHAIN_PROJECT'] = os.getenv('LANGCHAIN_PROJECT')
os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')


# 2. Load GROQ Model

# In[4]:


model = ChatGroq(model = 'gemma2-9b-it', api_key = os.environ['GROQ_API_KEY'])


# 3. Create Prompt Template

# In[13]:


generic_template = "Convert the following into {language} language" 
prompt = ChatPromptTemplate.from_messages(
[
    ("system",generic_template),
    ("user","I am learning LECL and GROQ")

]

)


# 4. Output Parser

# In[14]:


parser = StrOutputParser()


# 5. Chain the process

# In[15]:


chain = prompt|model|parser


# In[ ]:


# chain.invoke({"language":"bengali"})


# 6. App Definition

# In[18]:


app = FastAPI(title = "Langchain Server", version= 1.0, description= "Simple API Server using Langchani runnable interfaces")


# 7. Chain Routes

# In[21]:


add_routes(
    app,
    chain,
    path = '/chain'
)


# In[22]:


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)


# In[ ]:




