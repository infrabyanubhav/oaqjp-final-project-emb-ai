"""Server Entry Point"""

from flask import Flask, request, jsonify
from emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector", methods=["POST"])
def emotion_detector_endpoint():
    """
    API endpoint to detect emotions from input text.

    Expects a JSON payload with the following structure:
    {
        "text": "Your text to analyze"
    }

    Returns:
        - 200: JSON response containing emotion scores and dominant emotion.
        - 400: JSON error message if 'text' is missing or the text is invalid.
    """
    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({"error": "Missing 'text' in request body"}), 400

    text_to_analyze = data["text"]
    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
