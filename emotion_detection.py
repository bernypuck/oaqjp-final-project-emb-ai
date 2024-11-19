import requests
import json

def emotion_detector(text_to_analyze): #define function to detect emotions

    # define the URL for the detector
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # create the payload for the detector
    myobj =  { "raw_document": { "text": text_to_analyze } }

    # set the headers and required model for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # create a POST request for the API with payload and headers
    response = requests.post(url, json = myobj, headers = header)
    
    # reformat the list into a dictonary
    relist = json.loads(response.text)

    # create an empty dictionary to fill with entries
    formatted_response = {}

    # parse entries into dictionary
    formatted_dict = relist['emotionPredictions'][0]['emotion'] 

    # calculate dominant emotion and add it to the dictionary
    dominant_emotion = max(formatted_dict, key=lambda x: formatted_dict[x])

    formatted_dict['dominant_emotion'] = dominant_emotion
    
    # print dictionary
    for key, value in formatted_dict.items():
        print(key + ":", value)