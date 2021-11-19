import speech_recognition

recongnizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("Say somethig: ")
    audio = recongnizer.listen(source)

# words = input("Say something: ").lower()

# if "hello" in words:
#     print("Hello to you too!")
# elif "how are you" in words:
#     print("I am well , thanks")
# elif "goodbye" in words:
#     print("Goodbye to you too!")
# else:
#     print("Huh?")

print("You said:")
print(recongnizer.recognize_google(audio))