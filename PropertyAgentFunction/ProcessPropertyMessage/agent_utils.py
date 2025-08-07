from openai import AzureOpenAI
import os
from azure.data.tables import TableServiceClient

client = AzureOpenAI(
    api_key=os.environ["AZURE_OPENAI_KEY"],
    api_version="2023-05-15",
    azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"]
)

AZURE_STORAGE_CONNECTION_STRING = os.environ["AZURE_STORAGE_CONNECTION_STRING"]
TABLE_NAME = "PropertyListings"

def extract_property_data(message: str) -> str:
    system_prompt = (
        "You are a helpful assistant that extracts structured real estate data from messages. "
        "Return a dictionary in this format: "
        "{'type': '2BHK', 'location': 'Paramakudi', 'area': '1000 sqft', 'price': '28 lakhs', 'contact': '9999988888'}"
    )

    try:
        print(f"🔎 Sending message to OpenAI: {message}")

        response = client.chat.completions.create(
            model="gpt-35-turbo",  # Use your deployment name
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": message}
            ],
            temperature=0.3,
            max_tokens=300
        )
        return response.choices[0].message.content.strip()

    except Exception as e:
        print(f"❌ Error during OpenAI call: {e}")
        return None

def save_to_table_storage(data: dict):
    try:
        table_service = TableServiceClient.from_connection_string(conn_str=AZURE_STORAGE_CONNECTION_STRING)
        table_client = table_service.get_table_client(table_name=TABLE_NAME)

        location = data.get('location', 'Unknown')
        contact = data.get('contact', '0000000000')

        entity = {
            'PartitionKey': location,
            'RowKey': contact,
            'type': data.get('type', ''),
            'area': data.get('area', ''),
            'price': data.get('price', '')
        }

        table_client.upsert_entity(entity=entity)
        print("✅ Data saved to Azure Table Storage.")
    except Exception as e:
        print(f"❌ Error saving to Table Storage: {e}")
