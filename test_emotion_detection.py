"""unittest"""

import unittest
from emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """
    Unit tests for the emotion_detector function in emotion_detection.py.

    This test class checks whether the emotion_detector function correctly identifies
    the dominant emotion for a set of predefined text statements. Each test verifies:
        1. The returned result is a dictionary.
        2. The 'dominant_emotion' key exists in the result.
        3. The dominant emotion matches the expected emotion for the given text.
    """

    def test_emotion_detection_statements(self):
        """
        Test emotion_detector with multiple example statements for different emotions.
        """
        statements = {
            "joy": "I am glad this happened",
            "anger": "I am really mad about this",
            "disgust": "I feel disgusted just hearing about this",
            "sadness": "I am so sad about this",
            "fear": "I am really afraid that this will happen",
        }

        for expected_emotion, text in statements.items():
            result = emotion_detector(text)
            self.assertIsInstance(result, dict)  # Sanity check: result must be a dict
            self.assertIn("dominant_emotion", result)  # Sanity check key exists
            self.assertEqual(result.get("dominant_emotion"), expected_emotion)


if __name__ == "__main__":
    unittest.main()
