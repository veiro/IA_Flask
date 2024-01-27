import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):

    def test_glad_statement(self):
        text_to_analyze = "I am glad this happened."
        result = emotion_detector(text_to_analyze)
        self.assertEqual(result['dominant_emotion'], 'joy')

    def test_mad_statement(self):
        text_to_analyze = "I am really mad about this."
        result = emotion_detector(text_to_analyze)
        self.assertEqual(result['dominant_emotion'], 'anger')

    def test_disgusted_statement(self):
        text_to_analyze = "I feel disgusted just hearing about this."
        result = emotion_detector(text_to_analyze)
        self.assertEqual(result['dominant_emotion'], 'disgust')

    def test_sad_statement(self):
        text_to_analyze = "I am so sad about this."
        result = emotion_detector(text_to_analyze)
        self.assertEqual(result['dominant_emotion'], 'sadness')

    def test_afraid_statement(self):
        text_to_analyze = "I am really afraid that this will happen."
        result = emotion_detector(text_to_analyze)
        self.assertEqual(result['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
