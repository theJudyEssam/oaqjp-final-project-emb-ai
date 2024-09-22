import requests
import json
def emotion_detector(text_to_analyze):
    URL =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    Headers =  {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    payload = {"raw_document": { "text": text_to_analyze } }

    response = requests.post(URL,json= payload, headers=Headers)

   

    if response.status_code == 200:
        response_text = response.text
        formatted_text = json.loads(response_text)
    elif response.status_code == 400:
        response_text = None
        formatted_text = None
        

    
    result = formatted_text["emotionPredictions"][0]["emotion"]
    return result

