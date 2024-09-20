import json
import os

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the raw data from the request
        data = request.get_data(as_text=True)

        # Log the received data
        print("Received POST data:")
        print(data)

        # Try to parse and pretty print JSON if possible
        try:
            json_data = json.loads(data)
            print("Parsed JSON data:")
            print(json.dumps(json_data, indent=2))
        except json.JSONDecodeError:
            print("Received data is not valid JSON")

        # Return a success response
        return (
            jsonify({"status": "success", "message": "Data received and logged"}),
            200,
        )
    else:
        # Handle GET request
        return jsonify({"Choo Choo": "Welcome to your Flask app 🚅"})


if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
