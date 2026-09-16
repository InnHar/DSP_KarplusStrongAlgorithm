# You have to implement Karplus Strong alogrithm, by the formula 
# y[n] = x[n] + a * y[n-M], where 0 < a < 1, x[n] is finite support, x[n] = y[n] = 0 if n < 0.
# 1) you have to create function which takes vector x, a, and N as length of output signal 
# and returns y[n]
# 2) you have to create function which generates random x vector, feeds it to previous function
# and saves y[n] output signal as .wav file
# 3) Using last function you have to create wav examples
import numpy as np
from simple_wav import *

def karplus_strong(x, a, N):
    assert 0 < a < 1, 'a must be strictly btw 0 and 1'
    M = len(x)
    y = np.zeros(N, dtype=np.float32)
    for i in range(N):
        x_val = x[i] if i < M else 0.0
        y_val = y[i - M] if i >= M else 0.0
        y[i] = x_val + a * y_val
    return y

def generate_and_save_pluck(filename, freq=440, sr=44100, a=0.6, duration=3):
    M = int(np.round(sr / freq))
    x = np.random.uniform(-1.0, 1.0, M).astype(np.float32)
    
    N = int(duration * sr)
    y = karplus_strong(x, a, N)

    data = (y * 32767).astype(np.int16)

    print("Saving the pluck at:", filename)
    write_audio(filename, sr, data)

    return y