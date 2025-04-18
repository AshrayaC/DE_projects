import openai

openai.api_key = api_key
models = openai.Model.list()
available_models = [model.id for model in models.data]
✨ Optional: Format the Prompt with Column Labels
Your model prompt would benefit from clarity—give it context like column headers. For example:

python
Copy
Edit
template="Given the following ISS location data (timestamp, latitude, longitude), identify any anomalies or outliers:\n\n{data}"
✅ Cleaned & Final Version (with fixes)
python
Copy
Edit
import requests
import os
import openai 
import pandas as pd
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI

# Set API Key securely
os.environ["OPENAI_API_KEY"] = "your-api-key-here"
api_key = os.getenv("OPENAI_API_KEY")

# Set OpenAI API key for openai module
openai.api_key = api_key

# Initialize LangChain OpenAI wrapper
llm = OpenAI(model="gpt-4", openai_api_key=api_key)

# Step 1: Extract ISS data
url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
data = response.json()

iss_data = {
    "timestamp": data["timestamp"],
    "latitude": float(data["iss_position"]["latitude"]),
    "longitude": float(data["iss_position"]["longitude"])
}
iss_df = pd.DataFrame([iss_data])

# Step 2: Fetch available models (Optional)
models = openai.Model.list()
available_models = [model.id for model in models.data]
print("Available Models:", available_models)

# Step 3: Detect anomalies using LangChain
prompt_template = PromptTemplate(
    input_variables=["data"],
    template="Given the following ISS location data (timestamp, latitude, longitude), identify any anomalies or outliers:\n\n{data}"
)

def detect_anomalies_with_langchain(dataframe):
    data_str = dataframe.to_string(index=False)
    prompt = prompt_template.format(data=data_str)
    response = llm.invoke(prompt)
    return response

anomalies = detect_anomalies_with_langchain(iss_df)
print("Anomalies Detected:", anomalies)

# Step 4: Clean Data (latitude bounds)
clean_data = iss_df[(iss_df['latitude'] > -90) & (iss_df['latitude'] < 90)]

# Step 5: Save to CSV
clean_data.to_csv('iss_location_data.csv', index=False)
print("Data saved successfully!")

#Invalid values (e.g., latitude not between -90 and 90)
#Sudden jumps in location (not realistic for ISS orbit)
#Wrong timestamps (out of order or duplicated)