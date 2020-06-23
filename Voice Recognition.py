from speech_recognition import Recognizer, Microphone

r = Recognizer()

with Microphone() as src:
    print("Speak...")
    audio = r.listen(src)
    txt = r.recognize_google(audio, language='pt-br')
    print(txt)
