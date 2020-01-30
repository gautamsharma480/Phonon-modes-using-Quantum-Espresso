grep 'freq ( ' k-freq.dat  -A 8  | cut -c 3-73 > file.dat
## 8 is number of atoms in above lines, you can change according to your system.
sed -i '/freq ( /d' file.dat 
## file.dat is the file which is read by dynmat.py. 
