import google.generativeai as genai
import speech_recognition as sr

# Replace with your actual API key
api_key = "AIzaSyDeALI4_eGmIgUWjohnpTMnCONk5d2XkrI"

# Configure genai with the API key
genai.configure(api_key=api_key)

# Set up the GenerativeModel
model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hey there!"},
        {"role": "model", "parts": "Hi! I'm Chinna Swamy, your AI friend. What’s up?"},
    ]
)

print("Chat with Chinna Swamy! Type 'exit' or 'quit' to end the chat.")
print("Listening...")

recognizer = sr.Recognizer()

# Interactive chat loop for speech input/output
while True:
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            user_input = recognizer.recognize_google(audio)
            print("You: " + user_input)
        except sr.UnknownValueError:
            print("Sorry, I could not understand what you said.")
            continue
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")
            continue

    if user_input.lower() in ["exit", "quit"]:
        print("Ending chat...")
        break

    # Check for note-taking command
    if "note my points" in user_input.lower() or "note it done" in user_input.lower():
        with open("notes.txt", "a") as file:
            file.write(user_input + "\n")  # Save what the user said in notes.txt
        print("Chinna Swamy: Noted your points.")
        continue

    # Send user input to the model
    response = chat.send_message(user_input)

    # Extract the message text
    if response.candidates:
        response_text = response.candidates[0].content.parts[0].text if response.candidates[0].content.parts else "Sorry, I don't have a response."
    else:
        response_text = "Sorry, I don't have a response."

    # Display the response
    print("Chinna Swamy: " + response_text)
