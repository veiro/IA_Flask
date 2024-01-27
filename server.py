from flask import Flask, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_endpoint():
    try:
        # Get the text from the request JSON
        data = request.get_json()
        text_to_analyze = data.get('text', '')

        # Run emotion detection
        result = emotion_detector(text_to_analyze)

        # Format the response
        response = {
            'anger': result.get('anger', 0.0),
            'disgust': result.get('disgust', 0.0),
            'fear': result.get('fear', 0.0),
            'joy': result.get('joy', 0.0),
            'sadness': result.get('sadness', 0.0),
            'dominant_emotion': result.get('dominant_emotion', 'unknown')
        }

        return jsonify(response)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
