import wave

def create_wav_file(filename, num_channels, sample_width, frame_rate, num_frames):
    """Creates a new WAV file with the specified parameters.

    Args:
        filename: The name of the file to create.
        num_channels: The number of audio channels (1 for mono, 2 for stereo, etc.).
        sample_width: The number of bytes per audio sample (e.g., 2 for 16-bit audio).
        frame_rate: The sampling rate in frames per second.
        num_frames: The total number of audio frames.
    """

    with wave.open(filename, 'wb') as wav_file:
        wav_file.setnchannels(num_channels)
        wav_file.setsampwidth(sample_width)
        wav_file.setframerate(frame_rate)
        wav_file.setnframes(num_frames)
        wav_file.writeframes(b'your audio data here')  # Replace with actual audio data

# Example usage:
create_wav_file("my_new_audio.wav", 2, 2, 44100, 10000)