import speech_recognition

recongnizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say somethig: ")
    audio = recongnizer.listen(source)
print("You said:")
print(recongnizer.recognize_google(audio))
