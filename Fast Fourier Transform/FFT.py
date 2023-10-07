import numpy as np
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt

# Load audio file
rate, audio = wav.read('my_audio.wav')

# Compute FFT
FFT = np.fft.fft(audio)
FFT_magnitude = np.abs(FFT)

# Plot magnitude
plt.plot(FFT_magnitude)
plt.title('Audio')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.show()

# Compute inverse FFT
IFFT = np.fft.ifft(FFT)

# Save reconstructed audio
wav.write('regenerated.wav', rate, np.real(IFFT).astype(np.int16))
