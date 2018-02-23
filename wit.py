#recognize speech using wit.ai api

import speech_recognition as sr
import paho.mqtt.client as mqtt

broker_address = "192.168.246.244"
print("creating wit mqtt client")
client = mqtt.Client("WIT")
client.connect(broker_address)

def wit():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something")
        audio = r.listen(source)

    WIT_KEY = "SNXNMCG36VX5WPBXJ72OERZRK3GBINE7"

    try:
        speech = r.recognize_wit(audio, key = WIT_KEY)
        if speech == "이전 메뉴" :
            client.publish("voice/command", "이전 메뉴로")
            print("Wit thinks you said" + speech)
        elif speech == "다음 메뉴" :
            client.publish("voice/command", "다음 메뉴로")
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))
    wit()
    // this allows wit.py to run continuously 
    
wit()
