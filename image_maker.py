#import numpy as np
#import librosa
#import librosa.display
#import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
#from mpl_toolkits.axes_grid1 import make_axes_locatable
#
## Load the audio file
#audio_file = 'harmonic_audio.wav'
#y, sr = librosa.load(audio_file)
#
## Find the tempo (beats per minute) and beats
#tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
#
## Create a figure and axis for the spectrogram
#fig, ax_spectrogram = plt.subplots(figsize=(10, 6))
#
## Function to update the animation
#def update(frame):
#    # Clear the previous frame
#    ax_spectrogram.clear()
#    
#    # Compute the spectrogram for the current frame
#    start_frame = int(frame * sr)
#    end_frame = int((frame + 1) * sr)
#    D = librosa.amplitude_to_db(np.abs(librosa.stft(y[start_frame:end_frame])), ref=np.max)
#    
#    # Plot the spectrogram
#    im = ax_spectrogram.imshow(D, aspect='auto', origin='lower', cmap='viridis')
#    
#    # Compute beat times within the current frame
#    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#    beat_times_in_frame = beat_times[(beat_times >= frame) & (beat_times < frame + 1)]
#
#    # Plot beat markers
#    ax_spectrogram.vlines(beat_times_in_frame, 0, sr / 2, colors='r', linestyles='-', linewidth=2, alpha=0.75)
#
## Create the animation
#ani = FuncAnimation(fig, update, frames=np.arange(0, len(y) / sr, 1), interval=1000 / sr)
#
## Add a colorbar
#divider = make_axes_locatable(ax_spectrogram)
#cax = divider.append_axes("right", size="5%", pad=0.05)
#plt.colorbar(im, cax=cax, format='%+2.0f dB')
#
#plt.title('Real-time Spectrogram with Beat Markers')
#plt.xlabel('Time (s)')
#plt.ylabel('Frequency (Hz)')
#
#plt.show()

import numpy as np
import librosa
import librosa.display
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Load the audio file
audio_file = 'percussive_audio.wav'
y, sr = librosa.load(audio_file)

# Find the tempo (beats per minute) and beats
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)

# Create a figure and axis for the spectrogram
fig, ax_spectrogram = plt.subplots(figsize=(10, 6))

# Function to update the animation
def update(frame):
    # Clear the previous frame
    ax_spectrogram.clear()
    
    # Compute the spectrogram for the current frame
    start_frame = int(frame * sr)
    end_frame = int((frame + 1) * sr)
    D = librosa.amplitude_to_db(np.abs(librosa.stft(y[start_frame:end_frame])), ref=np.max)
    
    # Plot the spectrogram
    librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=ax_spectrogram)
    
    # Compute beat times within the current frame
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)
    beat_times_in_frame = beat_times[(beat_times >= frame) & (beat_times < frame + 1)]

    # Plot beat markers
    ax_spectrogram.vlines(beat_times_in_frame, 0, sr / 2, colors='r', linestyles='-', linewidth=2, alpha=0.75)

# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, len(y) / sr, 1), interval=1000 / sr)

# Add a colorbar
dummy_img = np.zeros((10, 10))  # Dummy image for colorbar
cbar = plt.colorbar(ax_spectrogram.imshow(dummy_img, cmap='viridis'), ax=ax_spectrogram, format='%+2.0f dB')
cbar.set_label('Magnitude (dB)')

plt.title('Real-time Spectrogram with Beat Markers')
plt.xlabel('Time (s)')
plt.ylabel('Frequency (Hz)')

plt.show()