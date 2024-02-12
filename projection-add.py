import numpy as np
import matplotlib.pyplot as plt

dos = np.loadtxt('total-dos.dat')
energies = dos[:,0]
proj_dos = dos[:,1]
dos_Sn = dos[:,2] + dos[:,3] + dos[:,4] + dos[:,5]
dos_P = dos[:,6] + dos[:,7] + dos[:,8] + dos[:,9]
dos_S1 = dos[:,10] + dos[:,11] + dos[:,12] + dos[:,21]
dos_S2 = dos[:,13] + dos[:,14] + dos[:,15] + dos[:,16]  
dos_S3 = dos[:,17] + dos[:,18] + dos[:,19] + dos[:,20]  
dos_S = dos_S1 + dos_S2 + dos_S3

for i in range(0,len(energies)):
    print(energies[i], proj_dos[i], dos_Sn[i], dos_P[i], dos_S[i])
'''plt.plot(energies, proj_dos)
plt.plot(energies, dos_Sn, dos_P, dos_S)
plt.show()'''
