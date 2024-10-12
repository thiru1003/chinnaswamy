import google.generativeai as genai
import pyttsx3
import speech_recognition as sr

# Replace "YOUR_API_KEY" with your actual API key
api_key = "AIzaSyDeALI4_eGmIgUWjohnpTMnCONk5d2XkrI"

# Configure genai with the API key
genai.configure(api_key=api_key)

# Initialize the TTS engine
engine = pyttsx3.init()

# Set up the GenerativeModel
model = genai.GenerativeModel("gemini-1.5-flash")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hey there!"},
        {"role": "model", "parts": "Hi! I'm Chinna Swamy, your AI friend. What’s up?"},
    ]
)

# Initialize the speech recognizer
recognizer = sr.Recognizer()
mic = sr.Microphone()

print("Chat with Chinna Swamy! Say 'exit' or 'quit' to end the chat.")

# Interactive chat loop
while True:
    with mic as source:
        print("You: ", end="", flush=True)  # Prompt for speech input
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio = recognizer.listen(source)  # Listen for audio input
    
    try:
        # Recognize speech using Google Web Speech API
        user_input = recognizer.recognize_google(audio)
        print("You said:", user_input)

        if user_input.lower() in ["exit", "quit"]:
            print("Ending chat...")
            break

        # Send user input to the GenerativeModel and get a response
        response = chat.send_message(user_input)

        # Access the response content correctly using attribute access
        response_text = response.candidates[0].text if response.candidates else "Sorry, I don't have a response."

        print("Chinna Swamy says:", response_text)

        # Convert response text to audio and play it
        engine.say(response_text)
        engine.runAndWait()

    except sr.UnknownValueError:
        print("Sorry, I could not understand the audio.")
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
