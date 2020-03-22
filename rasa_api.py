import requests
import json

URL_INTENT = "http://localhost:5005/model/parse"
HEADERS_INTENT = {'content-type': "application/json"}
URL_ANSWER = "http://localhost:5005/webhooks/rest/webhook"
HEADERS_ANSWER = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "07e991cc-b3e5-9f1e-9b8f-f574881d2314"
}


def get_intent(question):
    intent_bool = True

    payload = {"text": str(question)}
    response = requests.request("POST", URL_INTENT, data=json.dumps(payload), headers=HEADERS_INTENT)
    content = json.loads(response.content)

    intent, confidence = content['intent']['name'], content['intent']['confidence']

    if intent == "faq_qa":
        intent_bool = False

    return {"bool": intent_bool, "intent": intent, "confidence": confidence}


def get_answer(question):
    payload = {"message": str(question)}
    response = requests.request("POST", URL_ANSWER, data=json.dumps(payload), headers=HEADERS_ANSWER)
    content = json.loads(response.content)

    res = content[0]['text']

    return {"response": res}