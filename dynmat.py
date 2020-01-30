import numpy as np
import os  
os.system('sh run.sh')
natoms = 8
nmodes = natoms*3
g1 = np.loadtxt('scf2.in')
print('ANIMSTEPS'+'   '+str(nmodes))
print('CRYSTAL')
print('PRIMVEC')
with open('primitive.dat') as inp:
	axis = inp.readlines()
for x in axis:
	prim_vec = x.split()
	# if position coordinates are given in angstrom then
	print(float(prim_vec[0][:]),float(prim_vec[1][:]),float(prim_vec[2][:]))
	# if position coordinates are given in bohr then  ,it will change to angstrom 
#	print(float(prim_vec[0][:])*0.529177,float(prim_vec[1][:])*0.529177,float(prim_vec[2][:])*0.529177)

print('PRIMCOORD  1')
print(str(natoms)+'  1')

def call_me(natoms):
	names = np.loadtxt('scf1.in', dtype = 'str')
	##print(names[0][2:4])
	natoms = 8  
	#n = range(0,3*natoms+1) # 51*3 = 153+1 
	l = 1
	for j in range(0,natoms*3): # 0,7803 + 1 
		f1 = np.loadtxt('file.dat')
		#print(j)
		for i in range(0,natoms):
			print(names[i][:], g1[i][0],' ',g1[i][1],' ',g1[i][2], f1[i+natoms*j][0],' ',f1[i+natoms*j][2],' ',f1[i+natoms*j][4])
		##	print(j,i)
		l = l + 1
		if l <= natoms*3:
			print('PRIMCOORD'+' '+str(l))
			print(str(natoms)+'  1')
call_me(natoms)
