import matplotlib.pyplot as plt
import pandas as pd

a,b,c,d,e = range(0,26),range(0,26),range(0,26),range(0,27),range(0,29)
i=0

# Alumina Sample
df_a = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\Standard - 30kV40mA.csv', usecols=[0,1], skiprows=a)
df_b = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\Standard - 45kV20mA.csv', usecols=[0,1], skiprows=b)
df_c = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\Standard - 45kV40mA.csv', usecols=[0,1], skiprows=c)

fig_1,ax = plt.subplots(3, sharex=True, sharey=True)
ax[0].plot(df_a['Angle'], df_a['Intensity'], linewidth=1, label='30kV 40mA')
ax[1].plot(df_b['Angle'], df_b['Intensity'], linewidth=1, label='45kV 20mA', color='orange')
ax[2].plot(df_c['Angle'], df_c['Intensity'], linewidth=1, label='45kV 40mA', color='green')
    
fig_1.suptitle('XRD of Aluminum Standard')
ax[2].set(xlabel=r'$2 \Theta$ (Degrees)')
ax[1].set(ylabel='Intensity (A.U.)')
for i in range(0,3):
    ax[i].legend()

fig_1.savefig('Standard.png', dpi=300)

# XRD Data
df_d = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\XRD.csv', usecols=[0,1], skiprows=d)

fig_2 = plt.figure()
plt.scatter(df_d['Angle'], df_d['Intensity'], s=1, color='red')
    
plt.title('XRD of Unknown Sample D')
plt.xlabel(r'$2 \Theta$ (Degrees)')
plt.ylabel('Intensity (A.U.)')

fig_2.savefig('XRD.png', dpi=300)

# EDS Data 
df_e = pd.read_csv (r'C:\Users\andre\Documents\GitHub\MSE-353-Lab-01\EDS.csv', skiprows=e, skipfooter=1, engine='python')

fig_3 = plt.figure()
plt.plot(df_e['Energy'], df_e['Counts'], linewidth=1, color='purple')
    
plt.title('EDS of Unknown Sample D')
plt.xlabel('Energy (keV)')
plt.ylabel('Counts')

fig_3.savefig('EDS.png', dpi=300)