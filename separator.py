#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 10:55:59 2024

@author: chrisrelyea
"""

import librosa
import soundfile as sf

# Load the audio file
audio_file = 'sample.wav'
y, sr = librosa.load(audio_file, sr=None)

# Perform harmonic-percussive source separation (HPSS)
harmonic, percussive = librosa.effects.hpss(y)

# Write separated audio to new files
sf.write('harmonic_audio.wav', harmonic, sr)
sf.write('percussive_audio.wav', percussive, sr)

