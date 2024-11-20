import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

from perio import interpol, per, per_ls, bandpower

# SINE
samples = 128
f_0 = 0.1

t = np.concatenate(([0], np.cumsum(np.random.rand(samples-1))))
y = np.sin(2 * np.pi * f_0 * t)

t_new, y_new, f = interpol(t, y, samples)

p = per(t_new, y_new, f, samples)

t_new_ls = t_new[1:]
y_ls = y[1:]

p_ls = per_ls(t_new_ls, y_ls, f, samples)

plt.figure()
plt.plot(t, y, label='signal')
plt.plot(t_new, y_new, label='interp')
plt.title("Signal")
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(f, p)
plt.title("Periodogram")
plt.grid()
plt.show()

plt.figure()
plt.plot(f[1:], p_ls)
plt.title("Periodogram Lomb-Scargle")
plt.grid()
plt.show()


# REAL
file_path = "../../chf206.dat"
# file_path="C:/Users/bartl/Downloads/chf206.dat"
hrv = pd.read_csv(file_path, delimiter='\t').values.ravel()
hrv = hrv[1000:7000]

sampl = len(hrv)
f_s = 360

t_r = np.concatenate(([0],np.cumsum(hrv)))
y_r = np.concatenate(([0], hrv))

t_new_r, y_new_r, f_r = interpol(t_r, y_r, sampl)

p_r = per(t_new_r, y_new_r, f_r, sampl)

t_new_ls_r = t_new_r[1:]
y_ls_r = y_r[2:]

p_ls_r = per_ls(t_new_ls_r, y_ls_r, f_r, sampl)

plt.figure()
plt.plot(t_r, y_r, label='signal')
plt.plot(t_new_r, y_new_r, label='interp')
plt.title("Signal HRV")
# plt.ylim([0.3, 0.8])
plt.legend()
plt.grid()
plt.show()

plt.figure()
plt.plot(f_r, p_r)
plt.title("Periodogram HRV")
# plt.ylim([0.0, 0.001])
plt.grid()
plt.show()

plt.figure()
plt.plot(f_r[1:], p_ls_r)
plt.title("Periodogram Lomb-Scargle HRV")
# plt.ylim([0.0, 0.001])
plt.grid()
plt.show()

hf_range = (0.15, 0.4)
lf_range = (0.04, 0.15)
vlf_range = (0.0033, 0.04)
ulf_range = (0, 0.0033)
tp_range = (0, 0.4)

# using Lomb-Scargle periodogram
hf_power = bandpower(f_r[1:], p_ls_r, hf_range)
lf_power = bandpower(f_r[1:], p_ls_r, lf_range)
vlf_power = bandpower(f_r[1:], p_ls_r, vlf_range)
ulf_power = bandpower(f_r[1:], p_ls_r, ulf_range)
tp_power = bandpower(f_r[1:], p_ls_r, tp_range)

lf_hf_ratio = lf_power / hf_power if hf_power != 0 else np.inf

print("Using Lomb-Scargle periodogram: ")
print("HF Power:", hf_power)
print("LF Power:", lf_power)
print("VLF Power:", vlf_power)
print("ULF Power:", ulf_power)
print("Total Power (TP):", tp_power)
print("LF/HF Ratio:", lf_hf_ratio)

# using periodogram with interpolation
hf_power = bandpower(f_r[1:], p_r[1:], hf_range)
lf_power = bandpower(f_r[1:], p_r[1:], lf_range)
vlf_power = bandpower(f_r[1:], p_r[1:], vlf_range)
ulf_power = bandpower(f_r[1:], p_r[1:], ulf_range)
tp_power = bandpower(f_r[1:], p_r[1:], tp_range)

lf_hf_ratio = lf_power / hf_power if hf_power != 0 else np.inf

print("Using periodogram with interpolation: ")
print("HF Power:", hf_power)
print("LF Power:", lf_power)
print("VLF Power:", vlf_power)
print("ULF Power:", ulf_power)
print("Total Power (TP):", tp_power)
print("LF/HF Ratio:", lf_hf_ratio)




# # Rysowanie widma mocy
# plt.figure(figsize=(10, 6))
# plt.plot(f_r[1:], p_ls_r)
# plt.axvspan(hf_range[0], hf_range[1], color='red', alpha=0.3, label='HF')
# plt.axvspan(lf_range[0], lf_range[1], color='blue', alpha=0.3, label='LF')
# plt.axvspan(vlf_range[0], vlf_range[1], color='green', alpha=0.3, label='VLF')
# plt.axvspan(ulf_range[0], ulf_range[1], color='purple', alpha=0.3, label='ULF')
# plt.title("Widmo mocy HRV")
# plt.xlabel("Częstotliwość [Hz]")
# plt.ylabel("Moc")
# plt.legend()
# plt.grid()
# plt.show()