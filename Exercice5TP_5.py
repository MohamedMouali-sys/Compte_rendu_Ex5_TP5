import numpy as np
import matplotlib.pyplot as plt

# Partie 1 : matrice de covariance
data = np.random.randn(100, 3)
cov_matrix = np.cov(data, rowvar=False)

# Partie 2 : transformation de Fourier
t = np.linspace(0, 1, 500)
signal = np.sin(2 * np.pi * 50 * t) + np.sin(2 * np.pi * 120 * t)
fft = np.fft.fft(signal)
freq = np.fft.fftfreq(len(t), d=t[1] - t[0])

plt.figure(figsize=(8, 4))
plt.plot(freq[:len(freq)//2], np.abs(fft)[:len(freq)//2])
plt.title("Spectre de fréquences")
plt.xlabel("Fréquence (Hz)")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

# Partie 3 : simulation de lancers de dés
dice1 = np.random.randint(1, 7, 1000)
dice2 = np.random.randint(1, 7, 1000)
sums = dice1 + dice2

plt.figure(figsize=(8, 4))
plt.hist(sums, bins=range(2, 14), align='left', rwidth=0.8)
plt.title("Histogramme des sommes de deux dés (1000 lancers)")
plt.xlabel("Somme")
plt.ylabel("Fréquence")
plt.grid()
plt.show()
