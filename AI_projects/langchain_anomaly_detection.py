import requests
import os
import openai 
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI  # Use only this

# Set OpenAI API Key securely
os.environ["OPENAI_API_KEY"] = "your-api-key-here"  # Use environment variable
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI client
client = openai.OpenAI(api_key=api_key)  # Correct usage

# Initialize LangChain Model
llm = OpenAI(model="gpt-4", openai_api_key=api_key)  # Use LangChain's OpenAI wrapper

# Step 1: Extract data from OpenNotify API
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
data = response.json()

# Extract latitude & longitude as FLOATS
iss_data = {
    "timestamp": data["timestamp"],
    "latitude": float(data["iss_position"]["latitude"]),
    "longitude": float(data["iss_position"]["longitude"])
}

# Convert to DataFrame
iss_df = pd.DataFrame([iss_data])

# Fetch available models
models = client.models.list()
available_models = [model.id for model in models.data]  # Correct way to access models
print("Available Models:", available_models)

# Step 2: Anomaly Detection using LangChain
prompt_template = PromptTemplate(
    input_variables=["data"],
    template="Given the following ISS location data, identify any anomalies or outliers:\n\n{data}"
)

def detect_anomalies_with_langchain(dataframe):
    data_str = dataframe.to_string(index=False)
    prompt = prompt_template.format(data=data_str)
    response = llm.invoke(prompt)  
    return response

anomalies = detect_anomalies_with_langchain(iss_df)
print("Anomalies Detected:", anomalies)

# Step 3: Data Cleaning (Latitude should be between -90 and 90)
clean_data = iss_df[iss_df['latitude'].between(-90, 90, inclusive="neither")]  # Fix inclusive parameter

# Step 4: Save Clean Data
clean_data.to_csv('iss_location_data.csv', index=False)
print("Data saved successfully!")
