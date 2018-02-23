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
        if speech == "설정 페이지" :
            client.publish("voice/command", "설정")
            print("Wit thinks you said" + speech)
        elif speech == "카메라 페이지":
            client.publish("voice/command", "카메라")
        elif speech == "파일 페이지" :
            client.publish("voice/command", "파일")
        elif speech == "이전 페이지":
            client.publish("voice/command", "이전메뉴")
        elif speech == "다음 페이지":
            client.publish("voice/command", "다음메뉴")
        elif speech == "사진 찍어 줘" or "사진 찍어줘" :
            client.publish("voice/command", "사진")
        elif speech == "동영상 촬영 시작해줘" :
            client.publish("voice/command", "영상시작")
        elif speech == "동영상 촬영 스탑해줘" :
            client.publish("voice/command", "영상스탑")
                
    except sr.UnknownValueError:
        print("Wit.ai could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Wit.ai service; {0}".format(e))
    wit()
wit()
