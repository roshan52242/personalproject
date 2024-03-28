import speech_recognition as sr


def listening_function():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source,0,8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio)
        return query

    except:
        return ""
    

if __name__ == "__main__":
    print(listening_function())