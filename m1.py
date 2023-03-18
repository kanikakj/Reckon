import speech_recognition as sr
from googletrans import Translator
# initialize the recognizer
r = sr.Recognizer()
# use microphone as the source of audio input
with sr.Microphone() as source:
    print("Speak now...")
    # adjust the energy threshold based on your microphone's ambient noise level
    r.adjust_for_ambient_noise(source)
    # listen to the speech and convert it to text
    audio_data = r.listen(source)
# recognize the speech
text = r.recognize_google(audio_data, language='hi-IN')
translator = Translator()
hindi_text = text
english_text = translator.translate(hindi_text, src='hi', dest='en')
# print the recognized text
print(text)
print(english_text.text)