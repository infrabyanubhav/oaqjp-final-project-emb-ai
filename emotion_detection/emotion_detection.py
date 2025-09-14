"""Emotion detection module using IBM Watson NLP API."""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Analyze the emotion of the input text.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        dict: A dictionary containing emotion scores and the dominant emotion.
              Returns None if the API request fails.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    json_data = {"raw_document": {"text": text_to_analyze}}

    try:
        response = requests.post(url, headers=headers, json=json_data, timeout=10)

        if response.status_code == 200:
            json_txt = json.loads(response.text)

            emotions = json_txt["emotionPredictions"][0]["emotionMentions"][0][
                "emotion"
            ]

            # Find dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            return {
                "anger": emotions.get("anger"),
                "disgust": emotions.get("disgust"),
                "fear": emotions.get("fear"),
                "joy": emotions.get("joy"),
                "sadness": emotions.get("sadness"),
                "dominant_emotion": dominant_emotion,
            }

        return {"message": response.status_code}

    except requests.RequestException as e:
        return {"message": str(e)}
