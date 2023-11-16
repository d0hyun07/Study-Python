import numpy as np
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import os

# sampling rate 1초를 몇개로 쪼개느냐
Fs = 48000.0

tlen = 3

Ts = 1/Fs

x_list = np .arange(0, tlen, Ts)

y = np.sin(2*np.pi*Fs*x_list)

plt.plot(x_list[:300], y[:300], color = "blue")

