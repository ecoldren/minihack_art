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

# import numpy as np
# import librosa
# import librosa.display
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation
# 
# # Load the audio file
# audio_file = 'percussive_audio.wav'
# y, sr = librosa.load(audio_file)
# 
# # Find the tempo (beats per minute) and beats
# tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
# 
# # Create a figure and axis for the spectrogram
# fig, ax_spectrogram = plt.subplots(figsize=(10, 6))
# 
# def draw_dance_move(ax):
#     
#         # fig, ax = plt.subplots()
# 
#     # Head
#     ax.add_patch(plt.Circle((0.5, 0.8), 0.05, color='black'))
# 
#     # Body
#     ax.plot([0.5, 0.5], [0.7, 0.4], color='black')
# 
#     # Right Arm
#     ax.plot([0.5, 0.6], [0.65, 0.55], color='black')  # Shoulder to Elbow
#     ax.plot([0.6, 0.65], [0.55, 0.5], color='black')  # Elbow to Hand
# 
#     # Left Arm
#     ax.plot([0.5, 0.4], [0.65, 0.55], color='black')  # Shoulder to Elbow
#     ax.plot([0.4, 0.35], [0.55, 0.5], color='black')  # Elbow to Hand
# 
#     # Right Leg
#     ax.plot([0.5, 0.55], [0.4, 0.3], color='black')  # Hip to Knee
#     ax.plot([0.55, 0.6], [0.3, 0.2], color='black')  # Knee to Foot
# 
#     # Left Leg
#     ax.plot([0.5, 0.45], [0.4, 0.3], color='black')  # Hip to Knee
#     ax.plot([0.45, 0.4], [0.3, 0.2], color='black')  # Knee to Foot
# 
#     # Set axis limits and hide axis
#     ax.set_xlim(0, 1)
#     ax.set_ylim(0, 1)
#     ax.axis('off')
# 
#     plt.show()
# 
# 
# # Function to update the animation
# def update(frame):
#     # Clear the previous frame
#     ax_spectrogram.clear()
#     
#     # Compute the spectrogram for the current frame
#     start_frame = int(frame * sr)
#     end_frame = int((frame + 1) * sr)
#     D = librosa.amplitude_to_db(np.abs(librosa.stft(y[start_frame:end_frame])), ref=np.max)
#     
#     # Plot the spectrogram
#     librosa.display.specshow(D, sr=sr, x_axis='time', y_axis='log', ax=ax_spectrogram)
#     
#     # Compute beat times within the current frame
#     beat_times = librosa.frames_to_time(beat_frames, sr=sr)
#     beat_times_in_frame = beat_times[(beat_times >= frame) & (beat_times < frame + 1)]
# 
#     # Plot beat markers
#     for beat_time in beat_times_in_frame:
#         draw_dance_move(ax_spectrogram)
#         # x_pos = np.random.uniform(0, librosa.get_duration(y=y))
#         # y_pos = np.random.uniform(0, sr)
#         # ax_spectrogram.scatter(beat_time, y_pos, color='r', marker='o', s=100)
# 
# # Create the animation
# ani = FuncAnimation(fig, update, frames=np.arange(0, len(y) / sr, 1), interval=1000 / sr)
# 
# # Add a colorbar
# # dummy_img = np.zeros((10, 10))  # Dummy image for colorbar
# # cbar = plt.colorbar(ax_spectrogram.imshow(dummy_img, cmap='viridis'), ax=ax_spectrogram, format='%+2.0f dB')
# # cbar.set_label('Magnitude (dB)')
# 
# plt.title('Real-time Spectrogram with Beat Markers')
# plt.xlabel('Time (s)')
# plt.ylabel('Frequency (Hz)')
# 
# plt.show()

import numpy as np
import librosa
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import soundfile as sf

# Load the audio file
audio_file = 'sample.wav'
y, sr = librosa.load(audio_file, sr=None)

# Perform harmonic-percussive source separation (HPSS)
harmonic, percussive = librosa.effects.hpss(y)

# Write separated audio to new files
sf.write('harmonic_audio.wav', harmonic, sr)
sf.write('percussive_audio.wav', percussive, sr)

# # Load the audio file
audio_file = 'percussive_audio.wav'
y, sr = librosa.load(audio_file)
# 
# # Find the beats
tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr, hop_length=512, start_bpm=60)

# Create a figure and axis for the animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Function to draw the dancing figure
def draw_dance_move(pose):
        # fig, ax = plt.subplots()
    ax.clear()
    if pose == 0:
        # Head
        ax.add_patch(plt.Circle((0.5, 0.8), 0.05, color='black'))
        # Body
        ax.plot([0.5, 0.5], [0.7, 0.4], color='black')
        # Right Arm
        ax.plot([0.5, 0.6], [0.65, 0.55], color='black')  # Shoulder to Elbow
        ax.plot([0.6, 0.65], [0.55, 0.5], color='black')  # Elbow to Hand
        # Left Arm
        ax.plot([0.5, 0.4], [0.65, 0.55], color='black')  # Shoulder to Elbow
        ax.plot([0.4, 0.35], [0.55, 0.5], color='black')  # Elbow to Hand
        # Right Leg
        ax.plot([0.5, 0.55], [0.4, 0.3], color='black')  # Hip to Knee
        ax.plot([0.55, 0.6], [0.3, 0.2], color='black')  # Knee to Foot
        # Left Leg
        ax.plot([0.5, 0.45], [0.4, 0.3], color='black')  # Hip to Knee
        ax.plot([0.45, 0.4], [0.3, 0.2], color='black')  # Knee to Foot
    if pose == 1:
        # Head
        ax.add_patch(plt.Circle((0.5, 0.8), 0.05, color='black'))
        # Body
        ax.plot([0.5, 0.5], [0.7, 0.4], color='black')
        # Right Arm
        ax.plot([0.5, 0.6], [0.65, 0.45], color='black')  # Shoulder to Elbow
        ax.plot([0.6, 0.65], [0.45, 0.5], color='black')  # Elbow to Hand
        # Left Arm
        ax.plot([0.5, 0.4], [0.65, 0.55], color='black')  # Shoulder to Elbow
        ax.plot([0.4, 0.35], [0.55, 0.5], color='black')  # Elbow to Hand
        # Right Leg
        ax.plot([0.5, 0.55], [0.4, 0.3], color='black')  # Hip to Knee
        ax.plot([0.55, 0.6], [0.3, 0.2], color='black')  # Knee to Foot
        # Left Leg
        ax.plot([0.5, 0.45], [0.4, 0.3], color='black')  # Hip to Knee
        ax.plot([0.45, 0.4], [0.3, 0.2], color='black')  # Knee to Foot

    # Set axis limits and hide axis
    # ax.set_xlim(0, 1)
    # ax.set_ylim(0, 1)
    # ax.axis('off')

    # Decorations (optional)
    ax.text(0.5, 0.05, 'DANCE!', fontsize=12, ha='center')

# Function to update the animation
def update(frame):
    # Clear the previous frame
    ax.clear()
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')
    # Draw the dancing figure at beat events
    pose = 0
    counter = 0  # Initialize counter
    for beat_frame in beat_frames:
        print('beat happened')
        if beat_frame / sr <= frame:
            counter += 1
            if counter == 4:  # Perform action every 4 beat frames
                pose = (pose + 1) % 2
                draw_dance_move(pose)
                counter = 0  # Reset counter


# Create the animation
ani = FuncAnimation(fig, update, frames=np.arange(0, len(y) / sr, 0.1), interval=100)

plt.title('Dancing Figure at Beat Events')
plt.show()