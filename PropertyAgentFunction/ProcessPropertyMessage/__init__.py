import logging
import azure.functions as func
import json
import ast
import sys

from .agent_utils import extract_property_data, save_to_table_storage

# Ensure stdout is UTF-8 (for emojis, etc.)
try:
    sys.stdout.reconfigure(encoding='utf-8')
except Exception:
    pass

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info("⚡ HTTP trigger function processed a request.")

    try:
        # Parse request body as JSON list
        req_body = req.get_json()

        if isinstance(req_body, list) and len(req_body) > 0:
            first_item = req_body[0]
            message = first_item.get("message")
        else:
            return func.HttpResponse(
                "❌ Invalid JSON format. Expected a list with at least one object containing 'message'.",
                status_code=400
            )

        logging.info(f"📨 Original Message: {message}")

        # Extract structured data
        extracted_text = extract_property_data(message)
        logging.info(f"🧠 Extracted: {extracted_text}")

        if extracted_text:
            try:
                # Convert string output to dictionary
                parsed_data = ast.literal_eval(extracted_text)

                # Save to Azure Table Storage
                save_to_table_storage(parsed_data)

                return func.HttpResponse(
                    json.dumps({"status": "success", "data": parsed_data}),
                    status_code=200,
                    mimetype="application/json"
                )
            except Exception as e:
                logging.error(f"❌ Error parsing extracted text to dict: {e}")
                return func.HttpResponse(
                    f"❌ Error parsing extracted text to dictionary: {e}",
                    status_code=500
                )
        else:
            return func.HttpResponse(
                "❌ No structured output returned from extraction.",
                status_code=400
            )

    except Exception as e:
        logging.error(f"❌ Exception: {e}")
        return func.HttpResponse(
            f"❌ Internal Server Error: {str(e)}",
            status_code=500
        )
