import speech_recognition as sr

recognizer = sr.Recognizer()
mic = sr.Microphone(device_index=1)  # Replace with your WO Mic index

try:
    with mic as source:
        print("Microphone is working. Say something:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        print("Got it! Now recognizing...")
        try:
            text = recognizer.recognize_google(audio)
            print("You said: " + text)
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
except Exception as e:
    print(f"Error accessing microphone: {e}")
