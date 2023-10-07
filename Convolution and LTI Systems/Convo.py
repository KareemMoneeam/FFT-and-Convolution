import numpy as np
import matplotlib.pyplot as plt

# Define the impulse response h[n] as an empty array of 99 element
h = np.zeros(99)
# filling h[n] with samples
for i in range(99):
    h[i] = 0.31752 * np.sin(0.314159 * (i - 49.00001)) / (i - 49.00001)
    h[i] *= (0.54 - 0.46 * np.cos(0.0641114 * i))

# Plot the impulse response h[n]
plt.plot(h)
plt.title('Impulse Response h[n]')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()
# Define the input signal x[n] (the delta function)
x = np.zeros(500)
x[0] = 1

# Plot the Delta signal
plt.plot(x)
plt.title('Impulse x[n] (Delta Signal)')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()

# Convolve x[n] with h[n] to get the output y[n]

y = np.convolve(x, h, mode='same')  # the output will be more like a spike because of the delta signal(sifting)

# Plot the output signal y[n]
plt.plot(y)
plt.title('Convolution Output Signal y[n]')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()

# Define the new signal x2[n]=sin(2pi*6n/500) + 0.5sin(2pi*44n/500)
n = np.arange(500)
x2 = 1 * np.sin(2 * np.pi * 6 * n / 500) + 0.5 * np.sin(2 * np.pi * 44 * n / 500)

# Plot the new signal x2[n]
plt.plot(n, x2)
plt.title('Test Signal x2[n]')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()
# Convolve x2[n] with h[n] to get the output y[n]
y2 = np.convolve(x2, h, mode='same')
# the output will be a smother signal but without the noise (high freq)

# Plot the output signal y[n]
plt.plot(y2)
plt.title('Convolution Output Signal y2[n]')
plt.xlabel('Sample Index')
plt.ylabel('Amplitude')
plt.show()
