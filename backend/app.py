from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from openai import OpenAI
import json
import logging
from config import property_list  # Import property_list from config.py

logging.basicConfig(level=logging.INFO)

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=openai_api_key)

app = Flask(__name__)
CORS(app)

operators = ["≠", "="]

@app.route('/analyze', methods=['POST'])
def analyze_text():
    try:
        data = request.get_json()
        if not data or 'text' not in data or not isinstance(data['text'], str) or not data['text'].strip():
            logging.error("Invalid input: 'text' field is missing or empty.")
            return jsonify({"error": "Invalid input. 'text' field must be a non-empty string."}), 400

        text = data['text']
        logging.info(f"Received request with text: {text}")

        completion = client.chat.completions.create(
            model="gpt-4o-2024-08-06",
            messages=[
                {"role": "system", "content": "You are a highly skilled data analyst and text configuration expert. Your task is to analyze and configure data accurately, evaluate the appropriate return value based on the provided parameters and their values, and ensure comprehensive results."},
                {"role": "user", "content": "Your output must be in JSON format."},
                {"role": "user", "content": "Follow these steps to make your decision:"},
                {"role": "user", "content": f"Step 1. Break down the given text into numbered sections. The text is: {text}."},
                {"role": "user", "content": f"Step 2. For each numbered section, analyze the following dictionary of property names: {property_list}."},
                {"role": "user", "content": "Step 3. Determine which name value best describes the numbered section based on the provided dictionary."},
                {"role": "user", "content": f"Step 4. Analyze the 'parameters' key in the dictionary of property names and their values."},
                {"role": "user", "content": "Step 5. From the dictionary, compare the text in step 1 against the selector and select the appropriate selector."},
                {"role": "user", "content": "Step 6. Select the most appropriate selector based on the parameter values. Avoid selecting null when possible. Format and return as a string with a comma between the key and value."},
                {"role": "user", "content": f"Step 7. Format and return the selector as a key and value and confirm that it is a key value pair"},
                {"role": "user", "content": "Step 8. If the parameters are missing, invalid, or empty, return the `null:value` selector."},
                {"role": "user", "content": f"Step 9. Compare the text in step 1 with the selector in step 6 and choose from the following operators: {operators}."},
                {"role": "user", "content": f"Step 10. Select the description of the selected name in step 3."},
                {"role": "user", "content": "Step 11. return the associated id for each selected name from the property names disctionary."},
                {"role": "user", "content": "Step 11. For each section, return an array with the following structure: ['text', 'id, 'name', 'Operator', 'selector:value', 'description']."},
                {"role": "user", "content": "Step 12. If no property matches, return 'No matching property' and 'N/A' as placeholders."},
                {"role": "user", "content": "Step 13. Format the response as a JSON object where the keys are the numbers of the sections, and the values are the arrays described above."},
                {"role": "user", "content": "Step 14. Perform a thorough review of the generated JSON object to ensure that all selected names and descriptions are accurate, consistent with the input text, and aligned with the provided dictionary of properties."},
                {"role": "user", "content": "Step 15. If any inconsistencies, inaccuracies, or ambiguities are found during the review, correct them before finalizing the output."},
                {"role": "user", "content": "Step 16. Ensure the final JSON object is well-structured, properly formatted, and ready for downstream processing."},
                {"role": "user", "content": "Step 17. ensure that the final JSON is in the format ['text', 'id', 'name', 'Operator', 'selector:value', 'description']"}
            ],
            response_format={"type": "json_object"},
        )
        response_content = json.loads(completion.choices[0].message.content)
        logging.info("Response successfully generated.")
        print("Debug Response:", response_content)  # Debug print statement
        return jsonify(response_content)

    except json.JSONDecodeError:
        logging.error("Failed to decode JSON response from OpenAI.")
        return jsonify({"error": "Invalid response from OpenAI"}), 500
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        return jsonify({"error": "An unexpected error occurred"}), 500

@app.errorhandler(Exception)
def handle_exception(e):
    logging.error(f"Unhandled exception: {e}")
    return jsonify({"error": "An unexpected error occurred. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)
