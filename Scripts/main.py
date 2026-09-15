from simple_wav import *
from pathlib import Path
import os

root_path = Path.cwd()

path = root_path / "AudioFiles"/ "v5.wav"

print(f"The wave file path: {path}")

sr, audio_data = read_audio(path)

print(f"Power: {compute_power(audio_data)}")

print("Sampling rate: ", sr)

plot_waveform(audio_data, output_dir="plots", filename="v5_waveform.png")

plot_waveform(audio_data[50000:100000], output_dir="plots", filename="v5_waveform_segment.png")