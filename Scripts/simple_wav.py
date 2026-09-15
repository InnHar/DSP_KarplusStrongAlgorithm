import numpy as np
import scipy.io.wavfile as wavfile
import scipy.io
import itertools
import math
import time
#import adaptfilt as adf
import os
from scipy import signal
import matplotlib.pyplot as plt
import matplotlib.colors as colors
# from matplotlib.mlab import bivariate_normal
import glob
import subprocess

# file_path = 'v.wav'
# start = 16000
# end = 24000


# The function from the matplotlib.mlab was obsolete so I needed to replace it
def bivariate_normal(X, Y, sigmax=1.0, sigmay=1.0, mux=0.0, muy=0.0, sigmaxy=0.0):
    Xmu = X - mux
    Ymu = Y - muy
    rho = sigmaxy / (sigmax * sigmay)
    z = (Xmu**2 / sigmax**2 + Ymu**2 / sigmay**2 - 2 * rho * Xmu * Ymu / (sigmax * sigmay))
    return 1.0 / (2 * np.pi * sigmax * sigmay * np.sqrt(1 - rho**2)) * np.exp(-z / (2 * (1 - rho**2)))

def generate_sinusoidal_signal(freq, duration, path, sr=44100, amplitude=0.5):
    number_of_points = int(sr * duration)
    t = np.linspace(0, duration, number_of_points)
    data = amplitude * np.sin(2 * np.pi * freq * t)
    data_int16 = (data * 32767.0)
    write_audio(path, sr, data_int16)
    return None

# The function has been changed to return the sampling rate as well
def read_audio(path):
	# path: path of audio file with .wav extansion
	sr, data = wavfile.read(path)
	data = data.astype('float32')
	return sr, data

def write_audio(path, sr, data):
	# path: the path of output file,
	# sr: sampling rate
	# data: the audio waveform data
	data = data.astype('int16')
	wavfile.write(path, sr, data)
	return None

def compute_power(data):
	power = np.mean(data**2)
	return power

# Added the output_dir and the filename parameters to optionally save the plots.
def plot_waveform(data, sampling_frequency=None, output_dir=None, filename=None):
	# data: the audio waveform data
    if sampling_frequency:
        sampling_period = 1 / sampling_frequency
        time_points = sampling_period * np.arange(len(data))
        plt.plot(time_points, data)
        plt.ylabel('amplitude')
        plt.xlabel('time [s]')
        plt.title("Audio Waveform (Time Domain)")
    else:
        plt.plot(data)
        plt.ylabel('amplitude')
        plt.xlabel('samples')
        plt.title("Audio Waveform (Sample Index Domain)")

    if output_dir:
        os.makedirs(output_dir, exist_ok=True)
        save_path = os.path.join(output_dir, filename)
        plt.savefig(save_path)
    plt.show()

    return None

def change_sampling_rate(input_path, output_path, output_sr):
	# input_path: path of input audio file
	# output_path: path of output audio file
	# output_sr: sampling rate of output_path, integer
	assert input_path != output_path, 'input_path and output_path should not coincide'
	# make sure you have installed ffmpeg
	subprocess.call(['ffmpeg', '-i', input_path, '-ar', str(output_sr), output_path])
	return None

