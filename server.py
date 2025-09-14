"""Server Entry Point"""

from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    """Render the home page with the form."""
    return render_template("index.html")


@app.route("/emotionDetector", methods=["GET"])
def emotion_detector_endpoint():
    """
    API endpoint to detect emotions from input text using query parameters.

    Example request:
        GET /emotionDetector?textToAnalyze=Your+text+here

    Returns:
        - 200: JSON response containing emotion scores and dominant emotion.
        - 400: JSON error message if 'textToAnalyze' is missing or invalid.
    """
    text_to_analyze = request.args.get("textToAnalyze")

    if not text_to_analyze:
        return jsonify({"response":"Invalid text! Please try again!."})

    result = emotion_detector(text_to_analyze)

    if result.get("dominant_emotion") is None:
        return jsonify({"response": "Invalid text! Please try again!"}), 400

    return jsonify(result)




if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
