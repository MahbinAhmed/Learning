import pyttsx3

speaker = pyttsx3.init()
speaker.say("Hey There ! This is Hello World")
speaker.runAndWait()

# There's also a module named "gTTS" which is used to save a audio file made from text