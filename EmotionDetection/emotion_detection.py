import requests

def emotionByName(respose_json, name):
    return respose_json['emotionPredictions'][0]['emotion'][name]
def getGreater(respose_json):
    mayor=0
    sentiemtimientoMayor=''
    for sentimiento in ['anger','disgust','fear','joy','sadness']:
        if(respose_json['emotionPredictions'][0]['emotion'][sentimiento]>mayor):
            mayor=respose_json['emotionPredictions'][0]['emotion'][sentimiento]
            sentiemtimientoMayor=sentimiento
    return sentiemtimientoMayor

def emotion_detector(text_to_analyze):
    # URL for the Emotion Predict function
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Headers for the request
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    # Input JSON data
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        # Sending a POST request to the Emotion Predict function
        response = requests.post(url, json=input_json, headers=headers)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
           # Assuming the response is in JSON format
            response_json = response.json()

            # Build the output dictionary
            output_format = {
                'anger': emotionByName(response_json, 'anger'),
                'disgust': emotionByName(response_json, 'disgust'),
                'fear': emotionByName(response_json, 'fear'),
                'joy': emotionByName(response_json, 'joy'),
                'sadness': emotionByName(response_json, 'sadness'),
                'dominant_emotion': getGreater(response_json)
            }

            return output_format
        else:
            print('no dio 200')
            # Handle unsuccessful response (e.g., print error message)
            print(f"Error: {response.status_code} - {response.text}")
            return None
    except Exception as e:
        # Handle exceptions (e.g., connection error)
        print(f"Exception: {e}")
        return None

# Example usage:
# from final_project.emotion_detection import emotion_detector
# emotion_detector("I am feeling excited about this project!")
# emotion_detector("I am feeling excited about this project!")