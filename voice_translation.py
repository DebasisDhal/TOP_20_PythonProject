import googletrans
import speech_recognition

recognizer = speech_recognition.Recognizer()
with speech_recognition.Microphone() as source:
    print("speak now")
    voice = recognizer.listen(source)
    text = recognizer.recognize_google(voice,language="or")
    print(text)



translator = googletrans.Translator()
translation = translator.translate(text,dest="or")
print(translation)

#print(googletrans.LANGUAGES)

# pip install PyAudio