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
                {"role": "system", "content": "You are a highly skilled text analyst and configuration expert. Your task is to analyze and configure data accurately and comprehensively."},
                {"role": "user", "content": "Your output must be in JSON format."},
                {"role": "user", "content": f"Step 1: Break down the given text into numbered sections. The text is: {text}."},
                {"role": "user", "content": f"Step 2: For each numbered section, analyze the following dictionary of properties: {property_list}."},
                {"role": "user", "content": "Step 3: Determine which property key best describes each numbered section based on the provided dictionary."},
                {"role": "user", "content": "Step 4: For each section, return an array with the following structure: ['text', 'selected property key', 'description or value']."},
                {"role": "user", "content": "Step 5: If no property matches, return 'No matching property' and 'N/A' as placeholders."},
                {"role": "user", "content": "Step 6: Format the response as a JSON object where the keys are the numbers of the sections, and the values are the arrays described above."},
                {"role": "user", "content": "Step 7: Perform a thorough review of the generated JSON object to ensure that all selected property keys and descriptions are accurate, consistent with the input text, and aligned with the provided dictionary of properties."},
                {"role": "user", "content": "Step 8: If any inconsistencies, inaccuracies, or ambiguities are found during the review, correct them before finalizing the output."},
                {"role": "user", "content": "Step 9: Add a summary at the end of the JSON object that highlights the total number of sections analyzed, the number of matches found, and the number of unmatched sections."},
                {"role": "user", "content": "Step 10: Ensure the final JSON object is well-structured, properly formatted, and ready for downstream processing."}
            ],
            response_format={"type": "json_object"},
        )
        response_content = json.loads(completion.choices[0].message.content)
        logging.info("Response successfully generated.")
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
