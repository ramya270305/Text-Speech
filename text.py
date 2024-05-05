import moviepy.editor as mp
import speech_recognition as sr
# Load the video
video = mp.VideoFileClip(r"c:\Users\user\OneDrive\Desktop\text-speech\WhatsApp Video 2024-05-05 at 7.36.54 PM.mp4")
# Extract the audio from the video
audio_file = video.audio
audio_file.write_audiofile(r"c:\Users\user\OneDrive\Desktop\text-speech\example_audio.wav")
# Initialize recognizer
r = sr.Recognizer()
# Load the audio file
with sr.AudioFile(r"c:\Users\user\OneDrive\Desktop\text-speech\example_audio.wav") as source:
    data = r.record(source)
# Convert speech to text
text = r.recognize_google(data)
# Print the text
print("\nThe resultant text from video is:\n")
print(text)
