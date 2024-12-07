import numpy as np
import matplotlib.pyplot as plt
import wave
import struct
from processing.note_frequencies import get_note_frequency

"""
Parameter Definition: We define the frequency, sampling rate, and duration of the sine wave.
Time Samples: We create a time array using np.linspace to represent the time axis of the signal.
Sine Wave Generation: We use the formula for a sine wave to generate the audio data.
Plotting: We visualize the sine wave using Matplotlib.
Data Conversion: We convert the floating-point values to 16-bit integers, a common format for audio.
WAV File Writing: We use the wave module to create a WAV file, specifying the number of channels, sample width, frame rate, and writing the audio data.
This code creates a simple sine wave and saves it as a WAV file. You can experiment with different frequencies, amplitudes, and durations to create various audio signals.
"""
def create_sample(note, octave, duration):

    sampling_rate = 44100  # Samples per second
    frequency = get_note_frequency(note, octave)
    
    # Generate time samples
    time = np.linspace(0, duration, int(duration * sampling_rate), False)

    # Generate sine wave
    amplitude = 0.5
    sine_wave = amplitude * np.sin(2 * np.pi * frequency * time)

    # Convert to 16-bit integer format
    sine_wave_int = (sine_wave * 32767).astype(np.int16)

    # Write to a WAV file
    with wave.open(fr"..\sine_wave-{note}-{octave}-{duration}.wav", 'wb') as wav_file:
        wav_file.setnchannels(1)  # Mono
        wav_file.setsampwidth(2)  # 16-bit
        wav_file.setframerate(sampling_rate)
        wav_file.writeframes(b''.join(struct.pack('<h', x) for x in sine_wave_int))