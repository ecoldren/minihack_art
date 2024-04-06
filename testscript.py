import librosa
import numpy as np
import pygame
import sys

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

# Load an audio file
file_path = 'your_audio_file.mp3'
y, sr = librosa.load(file_path)

# Get the beat frames and tempo
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# Convert beat frames to timestamps
beat_times = librosa.frames_to_time(beat_frames, sr=sr)

# Main loop
running = True
beat_index = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Clear the screen
    screen.fill((0, 0, 0))
    
    # Check if we have a beat
    current_time = pygame.time.get_ticks() / 1000.0  # Convert milliseconds to seconds
    if beat_index < len(beat_times) and current_time >= beat_times[beat_index]:
        # Generate a random color for the beat
        color = (np.random.randint(0, 255), np.random.randint(0, 255), np.random.randint(0, 255))
        
        # Draw a circle at the center of the screen
        pygame.draw.circle(screen, color, (400, 300), 50)
        
        # Move to the next beat
        beat_index += 1
    
    # Update the display
    pygame.display.flip()

pygame.quit()
