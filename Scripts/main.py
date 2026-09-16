from simple_wav import *
from ks_implement import *
from pathlib import Path
import os

root_path = Path.cwd()

audiofile_dir = root_path / "AudioFiles"
audiofile_path =  audiofile_dir / "v5.wav"
audiofile_greater_volume_path = audiofile_dir / "twice_greater_volume.wav"
audio_low_sr_path = audiofile_dir / "audio_low_sr.wav"
sinusoidal_path = audiofile_dir / "sinusoid.wav"

# print(f"The wave file path: {audiofile_path}")

# sr, audio_data = read_audio(audiofile_path)

# print(f"Power: {compute_power(audio_data)}")

# print("Sampling rate: ", sr)

# plot_waveform(audio_data, output_dir="Plots", filename="v5_waveform.png")
# plot_waveform(audio_data[50000:100000], output_dir="Plots", filename="v5_waveform_segment.png")

# print("Writing new wav with 2 times greater volume. Saved in ", audiofile_greater_volume_path)
# louder_data = audio_data * 2.0
# if np.max(np.abs(louder_data)) > 32767:
#     louder_data = np.clip(louder_data, -32768, 32767)
# write_audio(audiofile_greater_volume_path, sr, louder_data)

# print("Decrease the audio sampling rate 2 times. Saved in ", audio_low_sr_path)
# change_sampling_rate(audiofile_path, audio_low_sr_path, sr//2)

# generate_sinusoidal_signal(440, 5, sinusoidal_path)
# _, sinusoidal_data = read_audio(sinusoidal_path)
# plot_waveform(sinusoidal_data, output_dir="Plots", filename="sinusoid.png")

freq = 440
sr = 44100
M = int(np.round(sr / freq))

y = generate_and_save_pluck(filename=audiofile_dir / "y_A4.wav", freq=440.0, a=0.99)
# generate_and_save_pluck(filename=audiofile_dir / "y_C4.wav", freq=261.63)
# generate_and_save_pluck(filename=audiofile_dir / "y_A2.wav", freq=110.0)

