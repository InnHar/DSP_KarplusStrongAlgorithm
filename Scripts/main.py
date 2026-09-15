from simple_wav import *
from pathlib import Path
import os

root_path = Path.cwd()

audiofile_dir = root_path / "AudioFiles"
audiofile_path =  audiofile_dir / "v5.wav"
audiofile_greater_volume = audiofile_dir / "twice_greater_volume.wav"
audio_low_sr = audiofile_dir / "audio_low_sr.wav"

print(f"The wave file path: {audiofile_path}")

sr, audio_data = read_audio(audiofile_path)

print(f"Power: {compute_power(audio_data)}")

print("Sampling rate: ", sr)

# plot_waveform(audio_data, output_dir="plots", filename="v5_waveform.png")
# plot_waveform(audio_data[50000:100000], output_dir="plots", filename="v5_waveform_segment.png")

print("Writing new wav with 2 times greater volume. Saved in ", audiofile_greater_volume)
louder_data = audio_data * 2.0
if np.max(np.abs(louder_data)) > 32767:
    louder_data = np.clip(louder_data, -32768, 32767)
write_audio(audiofile_greater_volume, sr, louder_data)

print("Decrease the audio sampling rate 2 times. Saved in ", audio_low_sr)
change_sampling_rate(audiofile_path, audio_low_sr, sr//2)
