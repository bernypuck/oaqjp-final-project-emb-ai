from EmotionDetection.emotion_detection import emotion_detector
import unittest

class TestEmotionDetector(unittest.case):
    def test_emotion_detector(self):
        
        result_1 = emotion_detector('I am glad this happened.')
        self.assertEqual(result_1['dominant_emotion'], 'joy')
        
        
unittest.main()