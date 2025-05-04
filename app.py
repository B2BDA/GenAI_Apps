from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel(model_name="gemini-1.5-pro")

def get_gemini_response(input, prompt):
    response = model.generate_content([input, "['TENCENT',\
    'ALIPAY*TAOBAO',\
    'HUDABEU-IPP10',\
    '101WATCHES']", prompt])
    return response.text


input_prompt = """"You have a very good understanding of the merchant names in hong kong and is expert in extracting the merchant
 names from the merchant list. Also you can indentify the installment plan tenor number as with very high accuracy. In addition to that 
 you are also good at differentiating a payment merchant and a non-payment merchant."""


response = get_gemini_response(input_prompt, "Please extract the retail merchant name, \
                               payment merchant name, \
                               tenor number from the list of merchant names in a table format like below:\n\n\
                                Original Mechant Name | Retail Merchant Name | Payment Merchant Name | Tenor Number.\" \
                                    Make it JSON format. \n\n\
                               ")
print(response)
