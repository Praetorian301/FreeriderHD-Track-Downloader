import os
import json
from flask import Flask, render_template, request, jsonify
import requests
import re

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fetch_data', methods=['POST'])
def fetch_data():
    data = request.get_json()
    url = data.get("url")
    
    # Extract track number from the provided FreeRider link
    match = re.search(r't/(\d+)-', url)
    if match:
        track_number = match.group(1)
    else:
        return jsonify({"error": "Invalid FreeRider link provided"}), 400

    # Construct the new URL
    generated_url = f"http://cdn.freeriderhd.com/free_rider_hd/tracks/prd/{track_number}/track-data-v1.js"
    
    # Fetch data from the generated URL
    try:
        response = requests.get(generated_url)
        response.raise_for_status()
        
        # Remove the "t(" prefix and closing ")" to convert to valid JSON
        track_data = response.text.strip("t();")
        track_json = json.loads(track_data)
        
        # Extract only the 'code' field
        code_output = track_json.get("code", "Code not found in track data")
    except requests.RequestException as e:
        return jsonify({"error": f"Failed to fetch data: {e}"}), 500
    except json.JSONDecodeError:
        return jsonify({"error": "Error parsing track data"}), 500

    return jsonify({"output": code_output})


if __name__ == "__main__":
    # Use the PORT environment variable if set, else default to 5000
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)