from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai
import json
load_dotenv()

genai.configure(api_key="")

model = genai.GenerativeModel(model_name="gemini-2.0-flash")

def get_gemini_response(input, prompt):
    response = model.generate_content([input, "['TENCENT',\
    'ALIPAY*TAOBAO',\
    'HUDABEU-IPP10',\
    '101WATCHES',\
    'CATHAPAC0000000245',\
    'CATHAP',\
    'FORTRESS-IPP2M',\
    'PEPPERSTON']", prompt])
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

input_prompt2 = """Given you are an expert in Hong Kong merchants, you are able to recognize similar merchant names and able to standardrize it.
Make sure the standardize names are correct and no errors are there."""

response2 = get_gemini_response(input_prompt2, f"""Please standardize the retail merchant name from {response}. \n\n\
                               Output in JSON format as below:
                                Original Mechant Name | Retail Merchant Name | Payment Merchant Name | Tenor Number | Standardized Merchant Name.
                               """)


print(response2)

with open('data2.json', 'w', encoding='utf-8') as f:
    json.dump(response2, f, ensure_ascii=False, indent=4)
