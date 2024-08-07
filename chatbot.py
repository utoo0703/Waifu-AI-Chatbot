import random
import speech_recognition as sr
import pyttsx3
from huggingface_hub import InferenceClient

# Initialize the recognizer and TTS engine
r = sr.Recognizer()
engine = pyttsx3.init()

# Function to convert text to speech
def SpeakText(command):
    engine.say(command)
    engine.runAndWait()

# Initialize the Inference Client for Mistral model
client = InferenceClient("mistralai/Mistral-7B-Instruct-v0.3")

system_instructions = "[SYSTEM] Generate a random description of properties of Anime named '{anime_name}'. {additional_instructions}"

def generate_description(anime_name, anime_features):
    additional_instructions = ""
    if anime_features:
        additional_instructions = f"with physical description '{anime_features}'"
    formatted_prompt = system_instructions.format(anime_name=anime_name, additional_instructions=additional_instructions)
    
    generate_kwargs = dict(
        max_new_tokens=300,
        do_sample=True,
    )
    
    stream = client.text_generation(formatted_prompt, **generate_kwargs, stream=True, details=True, return_full_text=False)
    output = ""
    for response in stream:
        output += response.token.text
    return output

# Function to check if age is greater than 18
def check_age(age_input):
    try:
        age = int(age_input)
        if age >= 18:
            return True
        else:
            SpeakText("Sorry, you must be 18 or older to use this service. Have a good day.")
            print("Sorry, you must be 18 or older to use this service. Have a good day.")
            exit()  # Exit the program
    except ValueError:
        SpeakText("Invalid age format. Please provide your age as a number. Have a good day.")
        print("Invalid age format. Please provide your age as a number. Have a good day.")
        exit()  # Exit the program

# Function to get user input with validation
def get_valid_input(prompt, validation_func):
    while True:
        user_input = get_user_input(prompt)
        if user_input is not None and validation_func(user_input):
            return user_input
        else:
            SpeakText("Sorry, I did not understand that. Please try again.")
            print("Sorry, I did not understand that. Please try again.")

# Validation function for yes/no inputs
def validate_yes_no(input_text):
    return input_text.lower() in ['yes', 'no']

# Function to get user input
def get_user_input(prompt):
    SpeakText(prompt)
    print(prompt)
    retries = 3  # Set the number of retries allowed
    while retries > 0:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.5)  # Adjust for noise with longer duration
            audio2 = r.listen(source2)
            try:
                recognized_text = r.recognize_google(audio2).lower()
                print("Recognized:", recognized_text)
                SpeakText("You said: " + recognized_text)
                return recognized_text
            except sr.UnknownValueError:
                retries -= 1
                if retries > 0:
                    SpeakText("Sorry, I did not understand that. Please try again.")
                    print("Sorry, I did not understand that. Please try again.")
                else:
                    SpeakText("Sorry, I couldn't understand your response.")
                    print("Sorry, I couldn't understand your response.")
                    return None
            except sr.RequestError as e:
                SpeakText("There was an error with the request. Please try again.")
                print(f"Could not request results; {e}")
                return None
    return None

# Function to generate a random name for the anime
def generate_random_name():
    adjectives = ['Mighty', 'Brave', 'Wise', 'Mysterious', 'Swift', 'Fierce', 'Noble']
    nouns = ['Dragon', 'Phoenix', 'Samurai', 'Wizard', 'Ninja', 'Knight', 'Sorcerer']
    return random.choice(adjectives) + ' ' + random.choice(nouns)

# Validation function for anime options
def validate_anime_choice(input_text, options):
    for option in options:
        if any(word in input_text for word in option.lower().split()):
            return option
    return None

def main():
    try:
        # Prompt for user inputs
        user_data = {}
        user_data["name"] = get_user_input("Please provide your name.")
        print("Name:", user_data["name"])
        
        age_input = get_valid_input("Your age, please.", check_age)
        user_data["age"] = age_input
        print("Age:", user_data["age"])
        
        # Get anime-related options from the user
        anime_options = ["Goku from Dragon Ball Z", "Naruto from Naruto", "Luffy from One Piece", "Ichigo from Bleach"]
        anime_options_prompt = "Please choose an anime character from the following options: " + ", ".join(anime_options)
        
        while True:
            anime_choice_input = get_user_input(anime_options_prompt)
            validated_choice = validate_anime_choice(anime_choice_input, anime_options)
            if validated_choice:
                user_data["anime_choice"] = validated_choice
                print("Anime Choice:", user_data["anime_choice"])
                break
            else:
                SpeakText("I didn't understand. Please choose again.")
                print("I didn't understand. Please choose again.")
        
        # Ask if the user wants to specify features for the anime character
        user_specify_features = get_valid_input("Do you want to specify any features for the anime character? (Yes/No)", validate_yes_no)
        anime_features = None
        if user_specify_features.lower() == 'yes':
            anime_features = get_user_input("Please specify the features you want for the anime character.")
            print("Anime Features:", anime_features)
            user_data["anime_features"] = anime_features
        
        # Generate anime details
        anime_name = generate_random_name()
        user_data["anime_name"] = anime_name

        # Generate the description using the chosen model
        anime_description = generate_description(anime_name, anime_features)

        # User-facing message
        user_message = f"YOUR ANIME IS GETTING READY. {anime_name} is owned by {user_data['name']}."
        print(user_message)
        SpeakText(user_message)

        # Output the LLM-generated description
        print("Anime Description:", anime_description)
        SpeakText(anime_description)
        
        # Store user data for later reference
        print("User Data:", user_data)
        
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        SpeakText("There was an error with the request.")
        
    except sr.UnknownValueError:
        print("Unknown error occurred")
        SpeakText("Sorry, I did not understand that.")

if __name__ == "__main__":
    main()
