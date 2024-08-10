# myVoiceAssistant
This is a simple voice assistant script written in Python, utilizing the pyttsx3, speech_recognition, wikipedia, and webbrowser libraries. The assistant, named "Jack," can perform various tasks based on voice commands.

                                                 FEATURES

Text-to-Speech: The script uses pyttsx3 for converting text to speech, making the assistant capable of responding verbally.

Speech Recognition: With the help of the speech_recognition library, the assistant can listen to voice commands and process them.

Wishing User: The assistant greets the user based on the time of day (morning, afternoon, evening).

Wikipedia Search: Jack can search Wikipedia for a query and read out a brief summary of the results.

Open Websites: The assistant can open commonly used websites like YouTube and Google in a web browser.

Play Music: Jack can play a random song from a specified directory on your system.

Tell Time: The assistant can provide the current time on request.

                                                 HOW IT WORKS

The script initializes the voice engine with the user's preferred voice settings.

The wish_me() function greets the user based on the time of day.

The take_command() function listens for voice input and converts it into text using Google's speech recognition.

Depending on the user's command, the assistant performs tasks like searching Wikipedia, opening websites, playing music, or telling the current time.

                                                 HOW TO RUN

Ensure that the required Python libraries (pyttsx3, speech_recognition, wikipedia, webbrowser) are installed.

Set the path to your music directory in the play music section.

Run the script, and the assistant will start listening for your commands.
