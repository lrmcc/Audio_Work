import wave

def read_wav_file(filename):
    """Reads a WAV file and returns its parameters and audio data.

    Args:
        filename: The name of the WAV file to read.

    Returns:
        A tuple containing the number of channels, sample width, frame rate, number of frames, and audio data.
    """

    with wave.open(filename, 'rb') as wav_file:
        num_channels = wav_file.getnchannels()
        sample_width = wav_file.getsampwidth()
        frame_rate = wav_file.getframerate()
        num_frames = wav_file.getnframes()
        audio_frames = wav_file.readframes(num_frames)

    return num_channels, sample_width, frame_rate, num_frames, audio_frames

# Example usage:
channels, width, rate, frames, data = read_wav_file("my_audio.wav")
print(f"Channels: {channels}, Width: {width}, Rate: {rate}, Frames: {frames}")