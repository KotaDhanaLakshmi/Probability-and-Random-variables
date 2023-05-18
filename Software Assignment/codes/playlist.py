import os
import random
import pygame

# Initialize Pygame
pygame.init()

# Specify the folder path
folder_path = '/home/kota/playlist'

# List all files in the folder
files = os.listdir(folder_path)

# Randomize the file list
random.shuffle(files)

for file_name in files:
    file_path = os.path.join(folder_path, file_name)

    # Load the sound file
    pygame.mixer.music.load(file_path)

    # Play the sound file
    pygame.mixer.music.play()

    # Wait until the sound finishes playing
    while pygame.mixer.music.get_busy():
        pass

# Quit Pygame
pygame.quit()

