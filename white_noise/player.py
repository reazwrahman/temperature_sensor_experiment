import pygame
import time

# Initialize pygame mixer
pygame.mixer.init()

# Load the MP3 file
pygame.mixer.music.load('output2.mp3')

# Play the MP3 file on a loop
pygame.mixer.music.play(loops=-1)

# Keep the script running to allow continuous playback
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Stop the music when the script is interrupted
    pygame.mixer.music.stop()

