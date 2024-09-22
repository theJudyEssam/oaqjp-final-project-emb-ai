from EDetection import emotion_detection
import unittest

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detection(self):
        result_1 = emotion_detection.emotion_detector("I am glad this happened");
        dominant = max(result_1, key=result_1.get)
        self.assertEqual(dominant, 'joy')

        result_2 = emotion_detection.emotion_detector("I am really mad about this")
        dominant1 = max(result_2, key=result_2.get)
        self.assertEqual(dominant1, 'anger')

        result_3 = emotion_detection.emotion_detector("I feel disgusted just hearing about this")
        dominant2 = max(result_3, key=result_3.get)
        self.assertEqual(dominant2, 'disgust')

        result_4 = emotion_detection.emotion_detector("I am so sad about this")
        dominant3 = max(result_4, key=result_4.get)
        self.assertEqual(dominant3, 'sadness')

        result_5 = emotion_detection.emotion_detector("I am really afraid that this will happen")
        dominant4 = max(result_5, key=result_5.get)
        self.assertEqual(dominant4, 'fear')

        

unittest.main()