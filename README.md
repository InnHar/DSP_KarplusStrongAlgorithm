# Signal Processing Lab

A collection of basic Digital Signal Processing (DSP) tasks implemented in Python, including waveform visualization, audio resampling, power computation, and signal generation.

---

# Setup & Installation
**1. Prerequisites**

Ensure you have Python 3.10+, Git, and FFmpeg installed on your system:
```bash
sudo apt update && sudo apt install -y ffmpeg
```
**2. Clone the Repository**

Clone the project repository and navigate into the project directory:
```bash
git clone git@github.com:InnHar/DSP_KarplusStrongAlgorithm.git
cd KarplusStrongAlgorithm
```
**3. Virtual Environment Setup**

Activate your Python virtual environment and install dependencies:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

# Usage
**1. Prepare Directory & Input File**

Ensure the required directories exist and place your target input WAV file (v5.wav) into the AudioFiles folder:
```bash
mkdir -p AudioFiles Plots
```

**2. Run the Processing Pipeline**

Run the main pipeline from the root of the project:
```bash
python Scripts/main.py
```

# Tasks Implemented

1) Compute power of the provided .wav file.
2) Create function which plots previously defined segment of data.
3) Study signal data (print various segments of signal).
4) Write new .wav with 2 times greater volume.
5) Decrease the audio sampling rate 2 times.
6) Write a function which generates a sinusoidal signal with the given frequency and saves it as .wav file.
