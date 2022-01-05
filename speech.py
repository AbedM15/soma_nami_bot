import speech_recognition as sr
from chat import get_response, bot_name

def capture_audio():
    r=sr.Recognizer()

    mic=sr.Microphone()
    with mic as source:
        audio=r.listen(source)

    try:
        text=r.recognize_google(audio)
        #os.system("say "+ 'I think you said, '+text+'!')
    except Exception as e:
        print(e)
        
    return text
    

