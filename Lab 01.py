import matplotlib.pyplot as plt
import scipy.signal as sig
import pandas as pd
import numpy as np

a,b,c,d,e = range(0,26),range(0,26),range(0,26),range(0,27),range(0,29)
i=0

# Alumina Sample
df_a = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\Standard' \
                    ' - 30kV40mA.csv', usecols=[0,1], skiprows=a)
df_b = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\Standard' \
                    ' - 45kV20mA.csv', usecols=[0,1], skiprows=b)
df_c = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\Standard' \
                    ' - 45kV40mA.csv', usecols=[0,1], skiprows=c)

fig_1,ax = plt.subplots(3, sharex=True, sharey=True, figsize=(5, 6), dpi=300)
ax[0].plot(df_a['Angle'], df_a['Intensity'], linewidth=1, label='30kV 40mA')
ax[1].plot(df_b['Angle'], df_b['Intensity'], linewidth=1, label='45kV 20mA', \
           color='orange')
ax[2].plot(df_c['Angle'], df_c['Intensity'], linewidth=1, label='45kV 40mA', \
           color='green')
    
fig_1.suptitle('XRD of Alumina Standard')
ax[2].set(xlabel=r'$2 \Theta$ (Degrees)')
ax[1].set(ylabel='Intensity (A.U.)')
for i in range(0,3):
    ax[i].legend()

fig_1.savefig('Standard.png')

# XRD Data
df_d = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\XRD.csv', \
                    usecols=[0,1], skiprows=d)

fig_2 = plt.figure(figsize=(6, 6), dpi=300)
plt.scatter(df_d['Angle'], df_d['Intensity'], s=1, color='red')
    
plt.title('XRD of Unknown Sample D')
plt.xlabel(r'$2 \Theta$ (Degrees)')
plt.ylabel('Intensity (A.U.)')

fig_2.savefig('XRD.png')

# EDS Data 
df_e = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\EDS.csv', \
                    skiprows=e, skipfooter=1, engine='python')

peaks_1 = sig.find_peaks(df_e['Counts'], prominence=35)
peaks_2 = sig.find_peaks(df_e['Counts'], prominence=19)
peaks = peaks_1[0][1:9]
peaks = np.append(peaks, peaks_2[0][29])

x_vals = pd.Series(df_e['Energy'][peaks]).array
y_vals = pd.Series(df_e['Counts'][peaks]).array
labels = (r'$O_{K \alpha}$', r'$Na_{K \alpha}$', r'$Al_{K \alpha}$',  \
          r'$Si_{K \alpha}$', r'$Au_{M \alpha}$', r'$Fe_{K \alpha}$', \
          r'$Fe_{K \beta}$', r'$Au_{L \alpha}$',  r'$Au_{L \beta}$')

print(1000 * x_vals)

fig_3 = plt.figure(figsize=(6, 6), dpi=300)
plt.plot(df_e['Energy'][range(0,1350)], df_e['Counts'][range(0,1350)], \
         linewidth=0.5, color='purple')
    
plt.title('EDS of Unknown Sample D')
plt.xlabel('Energy (keV)')
plt.ylabel('Counts')

for i in range(0,9):
    plt.annotate(labels[i], (x_vals[i], y_vals[i]), xytext=(0,3), \
                 textcoords='offset points', ha='center')

fig_3.savefig('EDS.png')

# ICP-OES Data
df_f = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\ICP-OES.csv')

element = pd.Series(df_f['Element']).array
sample_ppm = 2 *pd.Series(df_f['Sample D']).array * \
             pd.Series(df_f['Standard ppm']).array / \
            (pd.Series(df_f['Standard Before']).array + \
             pd.Series(df_f['Standard After']).array)
weight_percent = 500 * sample_ppm * pd.Series(df_f['Gravimetric Factor']).array \
               * 100 / (pd.Series(df_f['Sample Added']).array * 10**6)

composition = (element, weight_percent)

print(composition)