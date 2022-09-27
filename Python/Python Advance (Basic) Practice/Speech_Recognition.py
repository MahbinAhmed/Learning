import speech_recognition as sr

r = sr.Recognizer()
# mic_list = sr.Microphone.list_microphone_names()
# print(mic_list)
with sr.Microphone(sample_rate=48000, chunk_size=1024)as source:
    print("Say...")
    audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Sorry ! Couldn't understand audio.")
    except sr.RequestError:
        print("Sorry! Request couldn't be proccessed")

# A module named "alsamixer" is used for manipulating the microphone options