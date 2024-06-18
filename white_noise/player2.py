from playsound import playsound
import time

# Path to your MP3 file
mp3file = 'white_noise.mp3'  # Replace with your file path

# Function to play the sound in a loop
def play_sound_loop(file):
    try:
        while True:
            playsound(file)
    except KeyboardInterrupt:
        print("Playback interrupted by user.")

# Start playing the sound
play_sound_loop(mp3file)

